import cv2
import numpy as np

img = cv2.imread("imgs/penguins.jpg")

# To know the img properties:
print(img.shape)
    # Something like this should be printed: (height, width, dimentions)
    # Each dimention represents a color in RGB, however expect diferences with other scales


imgResize = cv2.resize(img, (320,240))
# IF we try to make it bigger, it will work, but distortion will appear

imgCropped = img[100:500, 200:500] #Height, then width
# What we are actually doing is modiffing its matrix form
# Also remember how with works in displays, is not like math

cv2.imshow("Normal", img)
cv2.imshow("resized", imgResize)
cv2.imshow("cropped", imgCropped)

cv2.waitKey(0)
cv2.destroyAllWindows()