import cv2
import numpy as np

#Create a black screen:
img = np.zeros((500,500,3), np.uint8)
                            # Unsigned int 8 bits

#SHAPES:

#Draw Lines
cv2.line(img, (50,50), (200,300), (125,125,0), 2) #Green-ish

#TO get dimentions, you would do:
width = img.shape[1]
height = img.shape[0]


cv2.line(img, (0,0), (width, height) , (0,0,250), 2) #REd line

# Draw rectangles:

# With matrix 
                        # GBR format
img [120:200, 100:250] = 250, 0, 0

# With openCV function
cv2.rectangle(img, (300,150), (470,450), (250,0,0), 3)


cv2.imshow("Figures", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
