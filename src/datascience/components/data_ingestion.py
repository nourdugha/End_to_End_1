import os
import urllib.request as request
import zipfile
import shutil
from src.datascience import logger
from src.datascience.entity.config_entity import DataIngestionConfig

## component-Data Ingestion

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    # Downloading the zip file
    def download_file(self):
        """
        Downloads file from URL or copies from local path based on configuration
        """
        # If use_local_data is true, copy file from local path to data directory
        if self.config.use_local_data:
            if not os.path.exists(self.config.local_data_file):
                # Copy file from local path to data directory
                shutil.copy2(self.config.local_data_path,self.config.local_data_file)
                logger.info(f"Local file copied from {self.config.local_data_path} to {self.config.local_data_file}")

            else:
                logger.info(f"File already exists")
            
            
        # If use_local_data is false, download file from URL
        else:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
                )
                logger.info(f"{filename} download! with following info: \n{headers}")
            else:
                logger.info(f"File already exists")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        if zipfile.is_zipfile(self.config.local_data_file):
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                logger.info(f"Extracted zip file to: {unzip_path}")
        else:
            # If it's not a zip file, we don't need to do anything since the file
            # is already in the correct location from the download_file step
            logger.info(f"File is not a zip file, using it as is in: {self.config.local_data_file}")