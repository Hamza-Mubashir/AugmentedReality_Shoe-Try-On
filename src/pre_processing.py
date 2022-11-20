import cv2

def rotation_hanlder(image):
    rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    #### Uncomment to view Rotated Image
    # cv2.imwrite('3Rotated.png', rotated)
    flipped = cv2.flip(rotated, 1)
    #### Uncomment to view Flipped Image
    # cv2.imwrite('4Flipped.png', flipped)
    return flipped
