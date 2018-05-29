import cv2
import numpy as np 

img = cv2.imread('logo.png', 0)

cv2.imwrite('grascal image logo.png', img)