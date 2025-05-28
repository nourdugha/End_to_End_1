from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            config=ConfigurationManager()
            data_transformation_config=config.get_data_transformation_config()
            data_transformation=DataTransformation(config=data_transformation_config)
            data_transformation.train_test_spliting()
        except Exception as e:
            raise e
