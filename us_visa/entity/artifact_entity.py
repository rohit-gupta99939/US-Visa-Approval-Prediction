from dataclasses  import dataclass

@dataclass
class DataIngestionArtifact:
    train_file_path:str
    test_file_path:str 

@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    drift_report_file_path: str


@dataclass
class DataTransformationArtifact:
    transformation_object_file_path:str
    transformation_train_file_path:str
    transformation_test_file_path:str 