import cv2
from src import run_detection

#### INPUT IMAGES HERE

# Input First Person Image here 
image = cv2.imread('1HumanImage.jpeg')
# Input Shoe Try On Image here
shoe = cv2.imread("2EditedShoe.png", cv2.IMREAD_UNCHANGED)

#### HANDLING OPERATIONS
run_detection.operation_handler(image, shoe)