from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pileline import DataTransformationPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


Stage_Name = "Data Ingestion"
try:
    logger.info(f">>>>>> stage {Stage_Name} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {Stage_Name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
    
Stage_Name = "Data Validation"
try: 
    logger.info(f">>>>>> stage {Stage_Name} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> stage {Stage_Name} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e

Stage_Name = "Data Transformation"
try:
    logger.info(f">>>>>> Stage {Stage_Name} started <<<<<<")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>> Stage {Stage_Name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

Stage_Name = "Model Training "
try:
    logger.info(f">>>>>> stage {Stage_Name} started <<<<<<")
    obj = ModelTrainerPipeline()
    obj.initiate_model_trainer()
    logger.info(f">>>>>> stage {Stage_Name} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e

Stage_Name = "Model Evaluation"

try:
    logger.info(f">>>>>> stage {Stage_Name} started <<<<<<")
    obj = ModelEvaluationPipeline()
    obj.initiate_model_evaluation()
    logger.info(f">>>>>> stage {Stage_Name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

