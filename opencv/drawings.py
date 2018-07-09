import cv2
import numpy as np

img= cv2.imread('guitar.jpg')

cv2.line(img,(0,0),(200,200),(100,222,0),2)
cv2.rectangle(img,(100,100),(200,200),(255,0,0),-3)
cv2.circle(img,(500,500),100,(0,0,255),-2)
cv2.imshow('drawshapes',img)
cv2.waitKey(0)
cv2.destroyAllWindows()