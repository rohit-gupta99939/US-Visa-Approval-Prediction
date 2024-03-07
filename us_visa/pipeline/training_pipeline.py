import sys
from us_visa.exception import UsvisaException
from  us_visa.logger import logging
from us_visa.components.data_ingestion import DataIngestion

from us_visa.entity.config_entity import (DataIngestionConfig, DataValidationConfig)
from us_visa.entity.artifact_entity import (DataIngestionArtifact, DataValidationArtifact)
from us_visa.components.data_validation import DataValidation


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()

    def start_data_ingestion(self) ->DataIngestionArtifact:
        try:
            logging.info("starting data ingestion")
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info("Exiting the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifact
        except Exception as e:
            raise UsvisaException(e,sys)
        

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        """Start data validation"""

        logging.info("Start data validation method of TrainPipeline class")
        try:
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=self.data_validation_config)

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Exiting the start_data_validation method of TrainPipeline class")
            return data_validation_artifact
        except Exception as e:
            raise UsvisaException(e,sys)
    

    def run_pipeline(self,)-> None:

        try:
            logging.info("Starting the pipeline")
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            logging.info("Exiting the run_pipeline method of TrainPipeline class")
        except Exception as e:
            raise UsvisaException(e,sys)