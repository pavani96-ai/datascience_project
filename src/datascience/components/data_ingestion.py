import urllib.request as request
import os
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    ## downloading the zipfile
    def download_file(self):
        if not os.path.exists(self.config.local_data_dir):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_dir
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists")


    ##unzipping the downloaded file
    def extract_zip_file(self):
        """
        zip_file_path: str
        Etracts the zip filw into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_dir, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            