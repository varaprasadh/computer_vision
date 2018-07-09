import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
         ret,frame=cap.read()
         hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


         lower_red=np.array([0,0,0])
         upper_red=np.array([180,100,255])



         mask=cv2.inRange(frame,lower_red,upper_red)
         res=cv2.bitwise_and(hsv,frame,mask=mask)
         gaussianblur=cv2.GaussianBlur(res,(15,15),0)

         cv2.imshow('gblur',gaussianblur)
         cv2.imshow('hsv',hsv)
         cv2.imshow('res',res)  
         cv2.imshow('mask',mask) 
         cv2.imshow('video',frame)
         ch=cv2.waitKey(1)
         if ch & 0xff == ord('q'):
             break
cap.release()
cv2.destroyAllWindows()
