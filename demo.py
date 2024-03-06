from us_visa.logger import logging
from us_visa.exception import UsvisaException
from us_visa.pipeline.training_pipeline import TrainPipeline
import sys


pipline = TrainPipeline()
pipline.run_pipeline()
