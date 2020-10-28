import cv2

img = cv2.imread("imgs/penguins.jpg")

# In openCV, RGB is actually BGR
                            # Colorspace RGB -> GRAY
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("GrayScale", imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()