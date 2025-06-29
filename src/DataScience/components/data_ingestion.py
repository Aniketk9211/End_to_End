from urllib import request
import os
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import DataIngestionconfig

class DataIngestion:
    def __init__(self,config:DataIngestionconfig) -> None:
        self.config = config
    
    # Downloading the Zip file
    def download_file(self) -> None:
        """
        Download the Zip file
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else: 
            logger.info(f"File already exists")

    def extract_zip_file(self) -> None:
        """
        zip_file_path: str
        Extracts the zip file into the data directoty
        function return None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
            
        logger.info(f"File extracted in {unzip_path}")