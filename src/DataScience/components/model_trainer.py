import pandas as pd
import joblib
from sklearn.linear_model import ElasticNet
from src.datascience.entity.config_entity import ModelTrainerConfig
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig) -> None:
        self.config = config

    def modeltrain(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_X = train_data.drop([self.config.targer_column], axis=1)
        train_y = train_data[[self.config.targer_column]]
        train_X = test_data.drop([self.config.targer_column], axis=1)
        train_y = test_data[[self.config.targer_column]]


        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state= 42)
        lr.fit(train_X,train_y)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))