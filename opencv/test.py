import cv2
import numpy as np
img=cv2.imread('guitar.jpg',1)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.imwrite('copy.jpg',img)
