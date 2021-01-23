import cv2
import numpy as np

img = cv2.imread("imgs/mountain.jpg")

def emptyfunc (arg1):
    pass
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

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create another window with sliders
cv2.namedWindow("Sliders")
cv2.resizeWindow("Sliders", 300, 100)
                                    # Normaly in Hue there are 
                                    # 360, but cv2 gets to 180
                                    #Args are default and max vals
cv2.createTrackbar("Hue Min", "Sliders", 1, 179, emptyfunc)
cv2.createTrackbar("Hue Max", "Sliders", 79, 179, emptyfunc)
cv2.createTrackbar("Sat Min", "Sliders", 64, 255, emptyfunc)
cv2.createTrackbar("Sat Max", "Sliders", 245, 255, emptyfunc)
cv2.createTrackbar("Val Min", "Sliders", 127, 255, emptyfunc)
cv2.createTrackbar("Val Max", "Sliders", 255, 255, emptyfunc)

while True:
    # Get slider values
    h_min = cv2.getTrackbarPos("Hue Min", "Sliders")
    s_min = cv2.getTrackbarPos("Sat Min", "Sliders")
    v_min = cv2.getTrackbarPos("Val Min", "Sliders")

    h_max = cv2.getTrackbarPos("Hue Max", "Sliders")
    s_max = cv2.getTrackbarPos("Sat Max", "Sliders")
    v_max = cv2.getTrackbarPos("Val Max", "Sliders")

    
    # Create a mask
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # Filter out that color
    mask = cv2.inRange(imgHSV, lower, upper)
    # Merge original and masked
    imgRes = cv2.bitwise_and(img, img, mask= mask)

    # Show imgs
    jointIMgs = stackImages(1, ([img,imgHSV], [mask, imgRes]))
    cv2.imshow("Results", jointIMgs)


    # Just to wait 1 mlsnd
    cv2.waitKey(1)
cv2.destroyAllWindows()