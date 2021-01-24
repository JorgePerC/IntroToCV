import numpy as np
import cv2


def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=1280,
    display_height=720,
    framerate=60,
    flip_method=0, ):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

def stackImages(scale,imgArray):
    """
    Recovered from: https://www.youtube.com/watch?v=WQeoO7MI0Bs
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

def emptyfunc(args):
    # Empty func
    pass

def createHSVTuner():
    cv2.namedWindow("HSV Tunner")
    cv2.createTrackbar("Hue Min", "HSV Tunner", 0, 179, emptyfunc)
    cv2.createTrackbar("Hue Max", "HSV Tunner", 179, 179, emptyfunc)
    cv2.createTrackbar("Sat Min", "HSV Tunner", 0, 255, emptyfunc)
    cv2.createTrackbar("Sat Max", "HSV Tunner", 255, 255, emptyfunc)
    cv2.createTrackbar("Val Min", "HSV Tunner", 0, 255, emptyfunc)
    cv2.createTrackbar("Val Max", "HSV Tunner", 255, 255, emptyfunc)

def getMaskMatrix():
    # Creates a mask from the tunner values
    h_min = cv2.getTrackbarPos("Hue Min", "HSV Tunner")
    s_min = cv2.getTrackbarPos("Sat Min", "HSV Tunner")
    v_min = cv2.getTrackbarPos("Val Min", "HSV Tunner")

    h_max = cv2.getTrackbarPos("Hue Max", "HSV Tunner")
    s_max = cv2.getTrackbarPos("Sat Max", "HSV Tunner")
    v_max = cv2.getTrackbarPos("Val Max", "HSV Tunner")

    # Create arrays 
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    return (lower, upper)

# Initialice CSI Camera
capture = cv2.VideoCapture(gstreamer_pipeline(flip_method=0, framerate=30), cv2.CAP_GSTREAMER)

# Place bars
createHSVTuner()


while True:
    
    succ, img = capture.read()
    
    # First we blur the image to better recognice elements:
    blured = cv2.GaussianBlur(img, (7,7), 2)

    # Convert capture to HSV
    # TODO: Is there a way to capture in HSV? 
    imgHSV = cv2.cvtColor(blured, cv2.COLOR_BGR2HSV)

    # Create mask
    lower, upper = getMaskMatrix()
    mask = cv2.inRange(imgHSV, lower, upper)

    # Merge HSV and blurred
    imgRes = cv2.bitwise_and(blured, blured, mask= mask)

    # Show images:
    jointImgs = stackImages(.6, ([blured], [imgRes]))
    cv2.imshow("Preview", jointImgs)

    # Just to wait 1 mlsnd and maybe exit with ESC
    if cv2.waitKey(1) & 0xFF == 27:
        capture.release()
        break

# TODO: Solve: 5 client objects still exists during shotdown

cv2.destroyAllWindows()

