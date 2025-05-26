from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValiadtion
from src.datascience import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValiadtion(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
        