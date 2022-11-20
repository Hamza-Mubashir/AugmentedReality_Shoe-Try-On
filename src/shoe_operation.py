import cv2
import cvzone
import numpy as np

def left_foot_keypoints(image, keypoints):
    point1 = int(keypoints[2]['X']*image.shape[1])
    point2 = int(keypoints[2]['Y']*image.shape[0])
    point3 = int(keypoints[7]['X']*image.shape[1])
    point4 = int(keypoints[7]['Y']*image.shape[0])
    return point1, point2, point3, point4

def right_foot_keypoints(image, keypoints):
    point1 = int(keypoints[2]['X']*image.shape[1])
    point2 = int(keypoints[2]['Y']*image.shape[0])
    point3 = int(keypoints[7]['X']*image.shape[1])
    point4 = int(keypoints[7]['Y']*image.shape[0])
    return point1, point2, point3, point4

def overlayPNG(imgBack, imgFront, pos=[0, 0]):
    hf, wf, cf = imgFront.shape
    hb, wb, cb = imgBack.shape
    *_, mask = cv2.split(imgFront)
    maskBGRA = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
    maskBGR = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    imgRGBA = cv2.bitwise_and(imgFront, maskBGRA)
    imgRGB = cv2.cvtColor(imgRGBA, cv2.COLOR_BGRA2BGR)

    imgMaskFull = np.zeros((hb, wb, cb), np.uint8)
    imgMaskFull[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = imgRGB
    imgMaskFull2 = np.ones((hb, wb, cb), np.uint8) * 255
    maskBGRInv = cv2.bitwise_not(maskBGR)
    imgMaskFull2[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = maskBGRInv

    imgBack = cv2.bitwise_and(imgBack, imgMaskFull2)
    imgBack = cv2.bitwise_or(imgBack, imgMaskFull)
    return imgBack

def left_operation(image, front_img, count, keypoints):
    point1, point2, point3, point4 = left_foot_keypoints(image, keypoints)

    cropped_image = image[point2:point4, point3:point1]

    # cropped_image = cv2.resize(cropped_image, interpolation = cv2.INTER_AREA)
    ## Uncomment to save cropped image
    #cv2.imwrite('7Cropping.png'+ '_{0}'.format(count)+'.png', cropped_image)
    ## Printing Shape of Cropped Image
    print("The shape of the cropped image is given as:" )
    print(cropped_image.shape)

    ## Resizing Image
    resized_image = cv2.resize(front_img, (cropped_image.shape[1],cropped_image.shape[0]))
    ## Overlaying Image
    img_overlayed = cvzone.overlayPNG(cropped_image, resized_image)
    # Uncomment to Write Image
    # cv2.imwrite('10Overlayed.png'+ '_{0}'.format(count)+'.png', img_overlayed)

    ## Rearranging Image Location
    image[point2:point4, point3:point1] = img_overlayed
    # Uncomment to Write Image
    # cv2.imwrite('11Final.png'+ '_{0}'.format(count)+'.png', image)

def right_operation(image, front_img, count, keypoints):
    point1, point2, point3, point4 = right_foot_keypoints(image, keypoints)
    cropped_image = image[point2:point4, point3:point1]

    # cropped_image = cv2.resize(cropped_image, interpolation = cv2.INTER_AREA)
    ## Uncomment to save cropped image
    #cv2.imwrite('7Cropping.png'+ '_{0}'.format(count)+'.png', cropped_image)
    ## Printing Shape of Cropped Image
    print("The shape of the cropped image is given as:" )
    print(cropped_image.shape)

    ## Resizing Image
    resized_image = cv2.resize(front_img, (cropped_image.shape[1],cropped_image.shape[0]))
    ## Overlaying Image
    img_overlayed = cvzone.overlayPNG(cropped_image, resized_image)
    # Uncomment to Write Image
    # cv2.imwrite('10Overlayed.png'+ '_{0}'.format(count)+'.png', img_overlayed)

    ## Rearranging Image Location
    image[point2:point4, point3:point1] = img_overlayed
    # Uncomment to Write Image
    cv2.imwrite('samples/AR_Shoe_Output.png', image)