import cv2
import numpy as np

#Load the color image
img = cv2.imread('logo.png', cv2.IMREAD_COLOR)

#Display Image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()