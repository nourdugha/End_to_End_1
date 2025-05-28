from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_training import ModelTrainer

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_training(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e
