import sys
from pandas import DataFrame
from sklearn.pipeline import Pipeline

from us_visa.exception import UsvisaException
from us_visa.logger import logging

class TargetValueMapping:
    def __init__(self):
        self.Certified:int = 0
        self.Denied:int = 1

    def _asdict(self):
        return self.__dict__
    def reverse_mapping(self):
        mapping_response = self._asdict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))
    

class USvisaModel:
    def __init__(self,preprocessing_object: Pipeline, trained_model_object:object):
        """
        """

        self.preprocessing_object = preprocessing_object
        self.trained_model_object = trained_model_object

    def predict(self,dataframe:DataFrame) -> DataFrame:
        """
        """
        logging.info("Entering predict method of USvisaModel class")
        try:
            logging.info("using trained model to get predictions")

            transformed_features = self.preprocessing_object.transform(dataframe)
            
            return self.trained_model_object.predict(transformed_features)
        except Exception as e:
            raise UsvisaException(e,sys)
        
    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"
    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"
    