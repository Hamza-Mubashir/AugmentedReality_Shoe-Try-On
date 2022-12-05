import cv2
import mediapipe as mp
from src import pre_processing
from src import shoe_operation

mp_drawing = mp.solutions.drawing_utils
mp_objectron = mp.solutions.objectron

def operation_handler(image, shoe):
    # For static images:
    with mp_objectron.Objectron(static_image_mode=False,
                                max_num_objects=2,
                                min_detection_confidence=0.3,
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

            point1 = int(keypoints[2]['X']*image.shape[1])
            point2 = int(keypoints[2]['Y']*image.shape[0])
            point3 = int(keypoints[7]['X']*image.shape[1])
            point4 = int(keypoints[7]['Y']*image.shape[0])

            image_width = image.shape[1]
            image_centre = image_width/2
            print("The image centre is: {0}".format(image_centre))

            #### Left Foot Operation Handler
            if point1 <= image_centre:
                print("Running Left Foot")
                image = shoe_operation.left_operation(image, shoe, count, point1, point2, point3, point4)
            #### Right Foot Operation Handler
            if point1 >= image_centre:
                print("Running Right Foot")
                right_shoe = cv2.flip(shoe, 1)
                image = shoe_operation.right_operation(image, right_shoe, count, point1, point2, point3, point4)
            # Updating Count
            count = count + 1
            # For Last Iteration Break
            if count == 2:
               cv2.imwrite('samples/AR_Shoe_Output.png', image)