import os
import mlflow.sklearn
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import mlflow
import mlflow.sklearn
import joblib
from urllib.parse import urlparse
import numpy as np
from src.datascience.utils.common import save_json
from pathlib import Path
from src.datascience.entity.config_entity import ModelEvaluationConfig
import dagshub

# os.environ["MLFLOW_TRACKING_URL"]="https://dagshub.com/aniketkj9211/End_to_End.mlflow"
# os.environ["MLFLOW_TRACKING_USERNAME"]="aniketkj9211"
# os.environ["MLFLOW_TRACKING_PASSWORD"]="f32fbf433d33fd1b13590d7072686bd1a341dadf"

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_matrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual,pred)

        return rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_X = test_data.drop(self.config.target_column,axis=1)
        test_y = test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type = urlparse(mlflow.get_tracking_uri()).scheme

        dagshub.init(repo_owner='aniketkj9211', repo_name='End_to_End', mlflow=True)
        with mlflow.start_run(run_name="ElasticNet"):
            predicted_quality = model.predict(test_X)

            (rmse, mae, r2) = self.eval_matrics(test_y, predicted_quality)
            scores = {'rmse': rmse, 'mae': mae, 'r2': r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(scores)

        if tracking_url_type != "file":
            mlflow.sklearn.log_model(model, name="model",registered_model_name="ElasticNetModel")

        else:
            mlflow.sklearn.log_model(model, name="model")    
