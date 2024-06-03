import os
import cv2
import pickle
import mediapipe as mp
from sign_language_conversion.entity.config_entity import (DataPickle)

class DataFetcher:
    def __init__(self, config:DataPickle):
        self.config = config
    
    def datapick(self):
        try: 
            mp_hands = mp.solutions.hands
            hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

            data = []
            labels = []
            for dir_ in os.listdir(self.config.data_raw):
                for img_path in os.listdir(os.path.join(self.config.data_raw, dir_)):
                    data_aux = []
                    x_ = []
                    y_ = []

                    img = cv2.imread(os.path.join(self.config.data_raw, dir_, img_path))
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

            with open(self.config.data_pickle, 'wb') as f:
                pickle.dump({'data': data, 'labels': labels}, f)

            return 'data.pickle'

        except Exception as e:
            raise e