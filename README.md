# US-Visa-Approval-Prediction

conda create -n venv python=3.8 -y 

conda activate venv

# create a mongodb cluster and set cluster credencials as env variables
ex: - export MONGODB_URL="mongodb+srv://<username>:<password>...."

# same add aws iam admin credentials
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
for windows set as env variable