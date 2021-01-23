import cv2
print ("OpenCV imported")

# To take a still, we first need to open the feed from the camera


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

"""
# This will work only with a USB camera
# It will automatically connecto to the main one if number 0
# If several cameras, just increment by one to find the desired one

capture = cv2.VIdeoCapture(0) 

#To set video dimentions
capure.set(3,640)
capture.set(4,480)

#Change exposure
capture.set(10, 500)
"""

# cap.set(n,n2) is not working, use 
# gstreamer arguments
capture = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
        #framerate=10, display_width = 640, display_height =  480


while True:
    succ, img = capture.read()
    cv2.imshow("CSI Camera", img)
    keyCode = cv2.waitKey(30) & 0xFF
    # Stop the program on the ESC key
    if keyCode == 27:
        break
cv2.destroyAllWindows()

# TODO: Add button and take photo