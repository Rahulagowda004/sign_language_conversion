# sign_language_conversion

## Workflows

1. Update config.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Rahulagowda004/sign_language_conversion

### STEP 01- Create a conda environment after opening the repository

```bash
python3 -m venv .venv
```

```bash
.venv\Scripts\activate
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up your local host and port
```

## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Rahulagowda004/Facial_review_system.mlflow \
MLFLOW_TRACKING_USERNAME=Rahulagowda004 \
MLFLOW_TRACKING_PASSWORD=d15121a9b37945a700eae5385a0ae54fa810a813 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Rahulagowda004/Facial_review_system.mlflow

export MLFLOW_TRACKING_USERNAME=Rahulagowda004

export MLFLOW_TRACKING_PASSWORD=d15121a9b37945a700eae5385a0ae54fa810a813

```