import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import tensorflow as tf
from pathlib import Path
from sign_language_conversion.entity.config_entity import TrainingConfig

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
        self.model = RandomForestClassifier(n_estimators=config.n_estimators)

    def train(self):
        data_path = Path(self.config.dataset_path)
        with open(data_path, 'rb') as f:
            data_dict = pickle.load(f)
            
        data = np.asarray(data_dict['data'])
        labels = np.asarray(data_dict['labels'])
        
        max_len = max(len(item) for item in data)
        data_padded = tf.keras.preprocessing.sequence.pad_sequences(data, maxlen=max_len, padding='post', dtype='float32')

        # Convert to numpy arrays
        data_padded = np.asarray(data_padded)
        labels = np.asarray(labels)
                    
        # Split the data into training and testing sets
        x_train, x_test, y_train, y_test = train_test_split(data_padded, labels, test_size=0.2, shuffle=True, stratify=labels)

        self.model.fit(x_train, y_train)

        y_predict = self.model.predict(x_test)
        score = accuracy_score(y_test, y_predict)

        print(f'{score * 100:.2f}% of samples were classified correctly!')

        model_save_path = Path(self.config.trained_model_path)
        with open(model_save_path, 'wb') as f:
            pickle.dump({'model.pkl': self.model}, f)

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )

    def save_model(self, path: Path, model: RandomForestClassifier):
        with open(path, 'wb') as f:
            pickle.dump(model, f)