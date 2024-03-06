import os
import sys
from pandas import DataFrame
import pandas as pd
from sklearn.model_selection import train_test_split

from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.exception import UsvisaException
from us_visa.logger import logging
from us_visa.data_access.usvisa_data import USvisaData

class DataIngestion:
    def __init__(self,data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):

        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise UsvisaException(e,sys)
        
    def export_data_into_feature_store(self)->DataFrame:

        try:
            logging.info("Exporting data from MongoDB")
            usvisa_data = USvisaData()
            dataframe = usvisa_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            logging.info(f"Data exported successfully, shape of dataframe :{dataframe.shape}")
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Save exported data into feature store file path :{feature_store_file_path}")

            return dataframe
        except Exception as e:
            raise UsvisaException(e,sys)
    
    def split_data_as_trint_test(self, dataframe: DataFrame)->None:

        logging.info("Entering split_data_as_trint_test method with dataframe")

        try:
            train_set, test_set = train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info(f"Data split successfully, shape of train set :{train_set.shape}")
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            
            logging.info(f"Exporting train and test file path.")
            train_set.to_csv(self.data_ingestion_config.training_file_path,index =False,header =True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index =False,header =True)
            logging.info(f"Exported train and test data")
        except Exception as e:
            raise UsvisaException(e,sys)
    
    def initiate_data_ingestion(self)-> DataIngestionArtifact:

        logging.info("Enterd initiate_data_ingestion method of data_ingestion class")

        try:
            dataframe = self.export_data_into_feature_store()
            logging.info("Got the data from mongodb")
            self.split_data_as_trint_test(dataframe)
            logging.info("Exited initiate_data_ingestion method of data_ingestion class")
            data_ingestion_artifact = DataIngestionArtifact(train_file_path=self.data_ingestion_config.training_file_path,
                                          test_file_path=self.data_ingestion_config.testing_file_path)
            logging.info(f"Data ingestion artifact:{data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise UsvisaException(e,sys)
