import cv2
import mediapipe as mp
from src import pre_processing
from src import shoe_operation

mp_drawing = mp.solutions.drawing_utils
mp_objectron = mp.solutions.objectron

def operation_handler(image, shoe):
    # For static images:
    with mp_objectron.Objectron(static_image_mode=True,
                                max_num_objects=2,
                                min_detection_confidence=0.2,
                                model_name='Shoe') as objectron:
        # Convert the BGR image to RGB and process it with MediaPipe Objectron.
        results = objectron.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        # Draw box landmarks.
        if not results.detected_objects:
            print(f'No box landmarks detected')
        print(f'Box landmarks:')
        count = 0
        points = []
        # Creating Image Copy
        annotated_image = image.copy()
        #### Running Pre Processing
        shoe = pre_processing.rotation_hanlder(shoe)

        for detected_object in results.detected_objects:
            mp_drawing.draw_landmarks(
                annotated_image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
            mp_drawing.draw_axis(annotated_image, detected_object.rotation,
                                detected_object.translation)
            image_width, image_height = image.shape[1], image.shape[0]
            landmark_point = []
            points = detected_object.landmarks_2d.landmark
            keypoints = []
            for data_point in points:
                keypoints.append({
                                    'X': data_point.x,
                                    'Y': data_point.y,
                                    })

            #### Left Foot Operation Handler
            if count == 0:
                shoe_operation.left_operation(image, shoe, count, keypoints)
            #### Right Foot Operation Handler
            if count == 1:
                shoe = cv2.flip(shoe, 1)
                shoe_operation.right_operation(image, shoe, count, keypoints)
            # Updating Count
            count = count + 1
            # For Last Iteration Break
            if count == 2:
                break