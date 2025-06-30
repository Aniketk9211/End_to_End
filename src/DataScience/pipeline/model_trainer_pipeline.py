from src.datascience.components.model_trainer import ModelTrainer
from src.datascience.config.configuration import ConfigurationManager
from src.datascience import logger


class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass

    def initiate_model_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.modeltrain()

Stage_Name = "Model Training "
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {Stage_Name} started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.initiate_model_trainer()
        logger.info(f">>>>>> stage {Stage_Name} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e


