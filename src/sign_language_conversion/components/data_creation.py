import os
import cv2
from sign_language_conversion.entity.config_entity import (DataCreation)

class Data_Creation:
    def __init__(self, config: DataCreation):
        self.config = config
        
    def capture_data(self):
        DATA_DIR = self.config.local_data_file
        number_of_classes = self.config.number_of_classes
        dataset_size = 100

        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        def find_working_camera_index():
            for index in range(5):
                cap = cv2.VideoCapture(index)
                if cap.isOpened():
                    cap.release()
                    return index
            return None

        camera_index = find_working_camera_index()
        if camera_index is None:
            print("Error: Could not find a working camera.")
            return

        cap = cv2.VideoCapture(camera_index)
        if not cap.isOpened():
            print("Error: Could not open video device.")
            return

        for j in range(number_of_classes):
            class_dir = os.path.join(DATA_DIR, str(j))
            if not os.path.exists(class_dir):
                os.makedirs(class_dir)

            print(f'Collecting data for class {j}')

            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Error: Failed to capture image.")
                    break

                cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
                cv2.imshow('frame', frame)
                if cv2.waitKey(25) == ord('q'):
                    break

            counter = 0
            while counter < dataset_size:
                ret, frame = cap.read()
                if not ret:
                    print("Error: Failed to capture image.")
                    break

                cv2.imshow('frame', frame)
                cv2.waitKey(20)
                cv2.imwrite(os.path.join(class_dir, f'{counter}.jpg'), frame)
                counter += 1

                if cv2.waitKey(1) & 0xFF == ord('s'):
                    break

        cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(5)