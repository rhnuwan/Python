import cv2
import numpy as np

#Load the color image
img = cv2.imread('logo.png', cv2.IMREAD_COLOR)
#Window is resizable (flag is cv2.WINDOW_AUTOSIZE or cv2.WINDOW_NORMAL)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
