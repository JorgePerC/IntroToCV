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
    cv2.createTrackbar("Hue Min", "HSV Tunner", 31, 179, emptyfunc)
    cv2.createTrackbar("Hue Max", "HSV Tunner", 63, 179, emptyfunc)
    cv2.createTrackbar("Sat Min", "HSV Tunner", 60, 255, emptyfunc)
    cv2.createTrackbar("Sat Max", "HSV Tunner", 156, 255, emptyfunc)
    cv2.createTrackbar("Val Min", "HSV Tunner", 195, 255, emptyfunc)
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

def getCenter(points: list):
    Xs = [ i[:, 0] for i in points]
    Ys = [ i[:, 1] for i in points]
    x = sum(Xs)/len(Xs)
    y = sum(Ys)/len(Ys)
    return (int(x), int(y))

def getContours(img, coloredImg):
    img2 = np.copy(coloredImg)
                                        # Retrieve outermost contours
                                        # Experiment with other RETR
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cont in contours:
        area = cv2.contourArea(cont)
        # Draw borders
                                    # To draw all of them (contour index)
                                        # Color, tickness
        cv2.drawContours(img2, cont, -1, (155,0,0), 2)
        
        # Area threshold, to avoid unwanted figures
        if area > 200:
            # Curvelength, aka perimeter
                                        # If the shapes are closed
            perimiter = cv2.arcLength(cont, True)
            # Get corners from shapes as points
                                                    # Resolution and closed
            pointsCorner = cv2.approxPolyDP(cont, 0.02*perimiter, True)
            
            # totalPoints = len(pointsCorner)
            # print("La figura tiene:", totalPoints)

            # Draw bounding box
            x, y, w, h = cv2.boundingRect(pointsCorner)
            cv2.rectangle(img2, (x,y), (x+w, y+h), (0,0,255), 2)
            centerX, centerY = getCenter(pointsCorner)
            cv2.putText(img2, "Center at x:{} y:{}".format(centerX, centerY), (centerX, centerY), cv2.FONT_HERSHEY_COMPLEX, .5, (255,255, 255))
    return img2
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

    # Find edges:
    imgCanny = cv2.Canny(imgRes, 50, 50)
    imgContours = getContours(imgCanny, imgRes)

    # Show images:
    jointImgs = stackImages(.6, ([blured], [imgContours]))
    cv2.imshow("Preview", jointImgs)

    # Just to wait 1 mlsnd and maybe exit with ESC
    if cv2.waitKey(1) & 0xFF == 27:
        capture.release()
        break

# TODO: Solve: 5 client objects still exists during shotdown

cv2.destroyAllWindows()

