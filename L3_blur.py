import cv2
import numpy as np

img = cv2.imread("imgs/penguins.jpg")

#BLur with Gaussian function
                                #KernelSize
                                # It has to be odd numbers, and both should be the same
imgBlur = cv2.GaussianBlur(img, (7,7), 0)
                        
#Edge detection with Canny func
                        # Threshold values
imgCanny = cv2.Canny(imgBlur, 50,70)

# To make the borders THICK Bois
kernel = np.ones((5,5), np.uint8)
    # more iterations -> thicker
imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1)

# To make borders thiner
imgEroded = cv2.erode(imgDialation, kernel, iterations= 2 )

cv2.imshow("Blured", imgBlur)
cv2.imshow("Borders", imgCanny)
cv2.imshow("Dilation", imgDialation)
cv2.imshow("Eroded", imgEroded)

cv2.waitKey(0)
cv2.destroyAllWindows()