from src.datascience.pipeline.prediction_pipeline import PredictionPipeline
from fastapi import FastAPI,Request
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import numpy as np
import uvicorn
import os


app = FastAPI()
router = APIRouter()
templates = Jinja2Templates(directory="templates")



@router.get("/",response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/training")
async def training():
    os.system("python main.py")
    return "Training completed"


@router.api_route("/predict",methods=["POST","GET"],response_class=HTMLResponse)
async def predict(request: Request):
    if request.method == "POST":
        try:
            form_data = await request.form()
            fixed_acidity = float(form_data["fixed_acidity"])
            volatile_acidity = float(form_data["volatile_acidity"])
            citric_acid = float(form_data["citric_acid"])
            residual_sugar = float(form_data["residual_sugar"])
            chlorides = float(form_data["chlorides"])
            free_sulfur_dioxide = float(form_data["free_sulfur_dioxide"])
            total_sulfur_dioxide = float(form_data["total_sulfur_dioxide"])
            density = float(form_data["density"])
            pH = float(form_data["pH"])
            sulphates = float(form_data["sulphates"])
            alcohol = float(form_data["alcohol"])

            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1,11)

            prediction_pipeline = PredictionPipeline()
            prediction = prediction_pipeline.predict(data)
            return templates.TemplateResponse("results.html",{"request":request,"prediction":str(prediction)})
        except Exception as e:
            print(f"Error during prediction: {e}")
    else:
        return templates.TemplateResponse("index.html", {"request": request})

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)

