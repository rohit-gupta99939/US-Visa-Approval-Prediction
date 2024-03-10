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
# step 15: write code for componeents/data_validation.py
-- inside the file we will write code for data drift of the data.
-- data drift :- Data drift refers to gradual changes in the statistical properties of data used for machine learning models. It arises from shifts in population, user behavior, or data collection processes, impacting model accuracy. Continuous monitoring is essential to detect drift, triggering model retraining to adapt to evolving patterns. Detection techniques involve comparing feature distributions or monitoring prediction errors. Robust data governance and adherence to ethical considerations are crucial. Addressing data drift ensures sustained model effectiveness in real-world scenarios, considering legal implications in regulated industries.
-- to messure data drift we use evidently.ai ml-ops package.
# step 16: write code for componeents/data_transformation.py
-- in this file we preprocess our data drop un nessesory columns. and create a package preprocess.pkl
# step 17: write code for componeents/model_trainer.py
-- in this file we train our model and tune hyper parameter and save our model in artifect folder.
# step 18: write code for componeents/model_evaluation.py
-- in this file we download the old model from aws and check performance betwing new model and old model .
# step 19: write code for componeents/model_pusher.py
-- if our new model is better than the old model this fill push the new model into aws
# step 20: write code for entity/estimator.py
-- this file use for preprocess and predict our local model
# step 21: write code for entity/s3_estimator.py
-- this file use for read model for aws , check model is present in aws , predict using that model and save model aws.
# step 22: write code for cloud_storage/aws_storage.py
-- This file contains all aws s3 related functions
# step 23: write code for pipeline/prediction_pipeline.py
-- this file is use for prediction
# step 24: write code for templates/usvisa.html
-- this file is the frontend for user application
# step 25: write code for static/css/style.css
-- this file is used for stylesheet for our usvisa.html
# step 26: write code for app.py
-- this file is our fast-api 

# step 27: write Dockerfile
# step 28: create .github/workflows/aws.yml
-- write instruction in aws.yml