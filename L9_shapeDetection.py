import cv2
import numpy as np

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
            totalPoints = len(pointsCorner)

            print("La figura tiene:", totalPoints)

            # Draw bounding box
            x, y, w, h = cv2.boundingRect(pointsCorner)
            cv2.rectangle(img2, (x,y), (x+w, y+h), (0,0,255), 2)
    return img2
    



img = cv2.imread("imgs/shape.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)

# Find Edges
imgCanny = cv2.Canny(imgBlur, 50, 50)

# Find contours
imgContours = getContours(imgCanny, img)



#Show images
cv2.imshow("Formas", img)
cv2.imshow("Formas2", imgCanny)
cv2.imshow("Formas3", imgBlur)
cv2.imshow("Formas4", imgContours)

cv2.waitKey(0)

cv2.destroyAllWindows()