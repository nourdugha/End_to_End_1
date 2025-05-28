from typing import List
from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_training_pipeline import ModelTrainingPipeline
class Pipeline:
    def __init__(self):
        pass

    def run_stage(self, stage_name: str, pipeline_obj: object, pipeline_method: str) -> None:
        """
        Execute a pipeline stage with proper logging and error handling
        """
        try:
            logger.info(f">>>>>> stage {stage_name} started <<<<<<")
            method = getattr(pipeline_obj, pipeline_method)
            method()
            logger.info(f">>>>>> stage {stage_name} completed <<<<<<")
        except Exception as e:
            logger.exception(f"Error in {stage_name}: {str(e)}")
            raise e

    def run_pipeline(self):
        """
        Execute all pipeline stages in sequence
        """
        stages = [
            {
                "name": "Data Ingestion Stage",
                "pipeline": DataIngestionTrainingPipeline(),
                "method": "initiate_data_ingestion"
            },
            {
                "name": "Data Validation Stage",
                "pipeline": DataValidationTrainingPipeline(),
                "method": "initiate_data_validation"
            },
            {
                "name": "Data Transformation Stage",
                "pipeline": DataTransformationTrainingPipeline(),
                "method": "initiate_data_transformation"
            },
            {
                "name": "Model Training Stage",
                "pipeline": ModelTrainingPipeline(),
                "method": "initiate_model_training"
            }
        ]

        for stage in stages:
            self.run_stage(
                stage_name=stage["name"],
                pipeline_obj=stage["pipeline"],
                pipeline_method=stage["method"]
            )

if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.run_pipeline()