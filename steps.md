# step 1: Create the environment
# step 2: write template.py file
-- setup.py will create the directory structure
# step 3: Create requirements.txt file
-- requirements.txt file contains the requirements which need to be installed
-- at the end of the requirements.txt file was written -e . it will run template.py file when we will install the requirements.txt file
# step 4: write code for setup.py which contains the version number and other details of our application.
# step 5: write code for logger inside logger/__init__.py
# step 6: write code for exception inside exception/__init__.py
# step 7: write code for utils inside utils/main_utils.py
-- we are writing common functions in this file which we will use all ouver our project.
# step 8: write code for constants/__init__.py
-- in this file we assign values to all the constant veriables which we will use globaly.
# step 9: write code for configuration/mongo_db_connection.py
-- in this file we establish the connection with MongoDB
# step 10: write code for data_access/usvisa_data.py
-- this file will stablish conncetion from mongodeb and read the data from collection and return a dataframe.
# step 11: write code for entity/config_entry.py
-- inside this file we will mention the configuration for training pipeline and data ingestion.
# step 12: write code for entity/artifact_entry.py
-- inside this file we will mention the configuration for the artifact
# step 13:write code for componeents/data_ingestion.py
-- inside this file we will save the data in local storage then split the data into train and test and store the data into local.
# step 14: write code for pipeline/training_pipeline.py
-- inside the file we will write code for start data ingetion.
