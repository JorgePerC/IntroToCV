import cv2
import numpy as np

img = cv2.imread("imgs/mountain.jpg")


def stackImages(scale,imgArray):
    """
    This fucntion stacks images. However, I did not build it.
    Recovered from: https://www.youtube.com/watch?v=WQeoO7MI0Bs
    To work properly, you should have rectangles (equal number
    of imgs per column or row)
    """
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


# Basic stacks:
"""
There is a problem using the numpy functions:
    You can't add images with different channels.
    You can't resize images.
"""

horizontal = np.hstack((img, img))

vertical = np.vstack((img, img))

cv2.imshow("hor stack NP", horizontal)
cv2.imshow("ver stack NP", vertical)

# Call funtion

scale = 0.5 # To make images bigger or smaller
hrArray = [img, img, img]


imgStack = stackImages(scale, (hrArray, hrArray))

cv2.imshow("Custom function", imgStack)


cv2.waitKey(0)
