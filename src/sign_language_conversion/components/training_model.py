import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from pathlib import Path
from sign_language_conversion.entity.config_entity import TrainingConfig

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
        self.model = RandomForestClassifier(
            n_estimators=config.n_estimators
        )

    def train(self):
        data_path = Path(self.config.dataset_path)
        with open(data_path, 'rb') as f:
            data_dict = pickle.load(f)

        data = np.asarray(data_dict['data'])
        labels = np.asarray(data_dict['labels'])

        # Check if the number of samples is sufficient for splitting
        if len(data) == 0 or len(labels) == 0:
            print("Error: Insufficient data for splitting.")
            return

        x_train, x_test, y_train, y_test = train_test_split(
            data, labels, test_size=0.2, shuffle=True, stratify=labels)

        # Check if the resulting train set will be empty
        if len(x_train) == 0 or len(y_train) == 0:
            print("Error: Insufficient data for training.")
            return

        self.model.fit(x_train, y_train)

        y_predict = self.model.predict(x_test)
        score = accuracy_score(y_test, y_predict)

        print(f'{score * 100:.2f}% of samples were classified correctly!')

        model_save_path = Path('model1.p')
        with open(model_save_path, 'wb') as f:
            pickle.dump({'model': self.model}, f)

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )

    def save_model(self, path: Path, model: RandomForestClassifier):
        with open(path, 'wb') as f:
            pickle.dump(model, f)