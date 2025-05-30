# End_to_End_1

### Workflows--ML Pipeline

1. Data Ingestion
2. Data Validation
3. Data Transformation-- Feature Engineering,Data Preprocessing
4. Model Trainer
5. Model Evaluation- MLFLOW,Dagshub

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py



# Notes (Data Ingestion):
1- To configure local dataset from your local disk you have to change the config.yaml file by make the use_local_data is true &  local_data_file: artifacts/data_ingestion/data.csv instead of local_data_file: artifacts/data_ingestion/data.zip

2- If you want to download the dataset from external URL you have to config two things make the  use_local_data is false &  local_data_file: artifacts/data_ingestion/data.zip

