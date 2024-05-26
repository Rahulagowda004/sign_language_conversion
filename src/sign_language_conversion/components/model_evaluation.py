from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
from urllib.parse import urlparse
import json
import pickle
import numpy as np
from pathlib import Path
from sign_language_conversion.entity.config_entity import EvaluationConfig

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    @staticmethod
    def load_model(path: Path):
        with open(path, 'rb') as file:
            model_dict = pickle.load(file)
        model = model_dict['model']
        return model

    def evaluation(self):
        with open(self.config.training_data, 'rb') as file:
            data_dict = pickle.load(file)
        
        data = np.asarray(data_dict['data'])
        labels = np.asarray(data_dict['labels'])

        x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

        self.model = self.load_model(self.config.path_of_model)
        self.y_pred = self.model.predict(x_test)
        self.score = accuracy_score(y_test, self.y_pred)
        self.save_score()

    def save_score(self):
        scores = {"accuracy": self.score * 100}
        with open('scores.json', 'w') as file:
            json.dump(scores, file)

    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"accuracy": self.score})

            if tracking_url_type_store != "file":
                # Register the model
                mlflow.sklearn.log_model(self.model, "SGC_CONVERTER", registered_model_name="RANDOM_FOREST")
            else:
                mlflow.sklearn.log_model(self.model, "model")