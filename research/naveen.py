import os
os.chdir("../")

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='google.protobuf.symbol_database')

import numpy as np
import pickle
import cv2
import mediapipe as mp

class HandGestureRecognition:
    def __init__(self):
        model_path = 'model/model.pkl'
        with open(model_path, 'rb') as file:
            model_dict = pickle.load(file)
        self.model = model_dict['model']

        self.cap = cv2.VideoCapture(0)

        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.hands = self.mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

        self.labels_dict = {
            0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I',
            9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q',
            17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
            25: 'Z', 26: 'del', 27: " ", 28: 'wait'
        }
        
        self.output_file = open('output.txt', 'w')  # Open file to save outputs

    def recognize_gesture(self):
        try:
            while True:
                data_aux = []
                x_ = []
                y_ = []

                ret, frame = self.cap.read()
                if not ret:
                    print("Error: Failed to grab frame.")
                    break

                H, W, _ = frame.shape

                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                results = self.hands.process(frame_rgb)
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        self.mp_drawing.draw_landmarks(
                            frame,
                            hand_landmarks,
                            self.mp_hands.HAND_CONNECTIONS,
                            self.mp_drawing_styles.get_default_hand_landmarks_style(),
                            self.mp_drawing_styles.get_default_hand_connections_style())

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

                    x1 = int(min(x_) * W) - 10
                    y1 = int(min(y_) * H) - 10

                    x2 = int(max(x_) * W) - 10
                    y2 = int(max(y_) * H) - 10

                    prediction = self.model.predict([np.asarray(data_aux)])

                    predicted_character = self.labels_dict[int(prediction[0])]

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                    cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                                cv2.LINE_AA)
                    
                    # Save prediction to file
                    self.output_file.write(predicted_character)

                cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'): #press "q" to terminate the camera
                    break

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            self.cap.release()
            self.output_file.close()  # Close the output file
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            
if __name__ == "__main__":
    recognizer = HandGestureRecognition()
    recognizer.recognize_gesture()