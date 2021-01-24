import cv2
import os
from os import listdir
from os.path  import isfile, join

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

def getPhotoName(filePath :str):
    photosFiles = 0

    for f in listdir(filePath):
        if "photo" in f:
            photosFiles += 1
    return "photo_{}.jpg".format(int (photosFiles))

# Get camera feedback
capture = cv2.VideoCapture(gstreamer_pipeline(flip_method=0, framerate=30), cv2.CAP_GSTREAMER)
    #framerate=10, display_width = 640, display_height =  480


while True:
    succ, img = capture.read()
    cv2.imshow("CSI Camera", img)
    keyCode = cv2.waitKey(3) & 0xFF
    
    # Take a photo when spacebar is pressed. 
    if keyCode == 32:
        cv2.putText(img, "Your Photo! :)", (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0))
        cv2.imshow("CSI Camera", img)
        
        # Get file path for archive
        filePath = __file__
        filePath = filePath[::-1]
        filePath = filePath[ filePath.find("/"): ]
        filePath = filePath[::-1]
        
        # Save image file
        os.chdir(filePath)
        cv2.imwrite(getPhotoName(filePath), img)
        
        cv2.waitKey(0)
        break
    
    # Stop the program on the ESC key
    if keyCode == 27:
        break


cv2.destroyAllWindows()