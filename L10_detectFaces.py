import cv2

# Create custom cascades
# TODO: Find the original files from openCV 
faceCascade = cv2.CascadeClassifier("faceRecogResources/haarcascade_frontalface_default.xml") 
img = cv2.imread("imgs/people.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                                        #Scale and minimum neighbours
                                        # Experiment on these!
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,255), 2)

cv2.imshow("Normal", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
