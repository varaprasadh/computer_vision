import cv2
import numpy as np

img=cv2.imread('opencv.png')
img_copy=img.copy()
hands=cv2.imread('hands.jpg',1)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
not_mask=cv2.bitwise_not(mask)
bit_and=cv2.bitwise_and(img,img,mask=mask)

hand_gray=cv2.cvtColor(hands,cv2.COLOR_BGR2GRAY)
_,hand_mask=cv2.threshold(hand_gray,100,255,cv2.THRESH_BINARY)
hands_and=cv2.bitwise_and(hands,hands,mask=hand_mask)

#overlays an image over other image by weightes (0 to 1)
weighted=cv2.addWeighted(gray,0.3,mask,0.7,1)
 
cv2.imshow('hands',hands_and)
cv2.imshow('original',img)
cv2.imshow('not mask',not_mask)
cv2.imshow('bit_and',bit_and)
cv2.imshow('weightes',weighted)
cv2.imshow('mask',mask)
cv2.imshow('gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


