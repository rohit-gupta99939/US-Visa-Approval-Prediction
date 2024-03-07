import os
import sys
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
from us_visa.logger import logging
from us_visa.exception import UsvisaException
import pymongo
import certifi

ca = certifi.where()

class MongoDBClint:
    """
    This class establishes the connection to the MongoDB
    before using the class assign environment variables MONGODB_URL and url values.
    """

    clint = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try :
            if MongoDBClint.clint is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                print(mongo_db_url)
                if mongo_db_url is None:
                    raise Exception(f"Environment key : {MONGODB_URL_KEY} is not set.")
                MongoDBClint.clint = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.clint = MongoDBClint.clint
            self.database = self.clint[database_name]
            self.database_name = database_name

            logging.info("MongoDB connection established")

        except Exception as e:
            logging.error(f"MongoDB connection error : {str(e)}")
            raise  UsvisaException(e,sys)
