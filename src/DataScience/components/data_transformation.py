import os 
from src.datascience import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.datascience.entity.config_entity import DataTransformationConfig


class DataTranformation():
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: you can add differnt data transformation technique such as Scaler, PCA and all
    
    def data_train_test_split(self):
        data = pd.read_csv(self.config.data_path)

        # split the data into training and testing sets. (0.75, 0.25) split.
        train, test = train_test_split(data, random_state=50)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        logger.info("Splited data into training and test sets")
        logger.info(f"Train_shape: {train.shape}")
        logger.info(f"Test_shape: {test.shape}")

        print(train.shape)
        print(test.shape)
        

