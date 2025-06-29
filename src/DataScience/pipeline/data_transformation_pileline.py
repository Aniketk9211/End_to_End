from src.datascience import logger
from src.datascience.components.data_transformation import DataTranformation
from src.datascience.config.configuration import ConfigurationManager
from pathlib import Path

Stage_Name = "Data Validation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path(r"artifact\data_validation\status.txt"), "r") as f:
                status = bool(f.read().split(" ")[-1])
            if status == True:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTranformation(config=data_transformation_config)
                data_transformation.data_train_test_split()
            else:
                raise Exception("Your data schema is not valid")
        except Exception as e:
            logger.exception(e)
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {Stage_Name} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> Stage {Stage_Name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

