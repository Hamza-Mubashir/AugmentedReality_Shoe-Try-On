import cv2
from src import run_detection

#### INPUT IMAGES HERE

# Input First Person Image here 
image = cv2.imread('samples/testing.jpg')
# Input Shoe Try On Image here
shoe = cv2.imread("samples/Shoe.png", cv2.IMREAD_UNCHANGED)

#### HANDLING OPERATIONS
run_detection.operation_handler(image, shoe)