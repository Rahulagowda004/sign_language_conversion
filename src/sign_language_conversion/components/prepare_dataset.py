import os
import pickle
import mediapipe as mp
import cv2
from sign_language_conversion.entity.config_entity import Preparedataset

class Prepare_dataset:
    def __init__(self, config: Preparedataset):
        self.config = config

    @staticmethod
    def _prepare_dataset(data_dir):
        mp_hands = mp.solutions.hands

        hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

        data = []
        labels = []
        for dir_ in os.listdir(data_dir):
            for img_path in os.listdir(os.path.join(data_dir, dir_)):
                data_aux = []

                x_ = []
                y_ = []

                img = cv2.imread(os.path.join(data_dir, dir_, img_path))
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                results = hands.process(img_rgb)
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        for i in range(len(hand_landmarks.landmark)):
                            x = hand_landmarks.landmark[i].x
                            y = hand_landmarks.landmark[i].y

                            x_.append(x)
                            y_.append(y)

                        for i in range(len(hand_landmarks.landmark)):
                            x = hand_landmarks.landmark[i].x
                            y = hand_landmarks.landmark[i].y
                            data_aux.append(x - min(x_))
                            data_aux.append(y - min(y_))

                    data.append(data_aux)
                    labels.append(dir_)

        return {'data': data, 'labels': labels}

    def save_data(self):
        data = self._prepare_dataset(self.config.dataset)

        with open(self.config.root_dir / 'data.pickle', 'wb') as f:
            pickle.dump(data, f)

