import cv2
import numpy as np

black=np.zeros([1080,1920,1],'uint8')
cv2.imshow('black',black)
print(black[0,0,: ])
white= np.ones([1080,1920,3],'uint16')
white *= (2**16-1)
cv2.imshow('hello world!',white)
print(white[0,0, : ])
cv2.waitKey(0)

cv2.destroyAllWindows()
