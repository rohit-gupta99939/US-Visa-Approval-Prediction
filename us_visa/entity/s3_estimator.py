from us_visa.cloud_storage.aws_storage import SimpleStorageService
from us_visa.exception import UsvisaException
from us_visa.entity.estimator import USvisaModel
import sys
from pandas import DataFrame
from us_visa.utils.main_utils import load_numpy_array_data,read_yaml_file,load_object,save_object


class USvisaEstimator:
    """
    This class is used to save and retrieve us_visas model in s3 bucket and to do prediction
    """

    def __init__(self,bucket_name,model_path):
        """
        :param bucket_name: Name of your model bucket
        :param model_path: Location of your model in bucket
        """
        self.bucket_name = bucket_name
        self.s3 = SimpleStorageService()
        self.model_path = model_path
        self.loaded_model:USvisaModel=None
    


    def is_model_present(self,model_path):
        try:
            return self.s3.s3_key_path_available(bucket_name=self.bucket_name, s3_key=model_path)
        except UsvisaException as e:
            print(e)
            return False

    def load_model(self,)->USvisaModel:
        """
        Load the model from the model_path
        :return:
        """

        return self.s3.load_model(self.model_path,bucket_name=self.bucket_name)

    def save_model(self,from_file,remove:bool=False)->None:
        """
        Save the model to the model_path
        :param from_file: Your local system model path
        :param remove: By default it is false that mean you will have your model locally available in your system folder
        :return:
        """
        try:
            self.s3.upload_file(from_file,
                                to_filename=self.model_path,
                                bucket_name=self.bucket_name,
                                remove=remove
                                )
        except Exception as e:
            raise UsvisaException(e, sys)


    def predict(self,dataframe:DataFrame):
        """
        :param dataframe:
        :return:
        """
        try:
            if self.loaded_model is None:
                self.loaded_model = self.load_model()
            print(self.loaded_model)
            # print(self.data_transformation_artifact)
            # print(self.data_transformation_artifact.transformation_object_file_path)
            # preprocessing_obj = load_object(file_path=self.data_transformation_artifact.transformation_object_file_path)
            result =self.loaded_model.predict(dataframe=dataframe)
            # print("preprocessing_obj :",preprocessing_obj)
            # usvisa_model = USvisaModel(preprocessing_object = preprocessing_obj, trained_model_object = self.loaded_model)
            # print("dataframe :", dataframe)
            # result =usvisa_model.predict(dataframe=dataframe)
            print("DBUG 01")
            return result
        except Exception as e:
            raise UsvisaException(e, sys)