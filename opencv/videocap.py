import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
          ret,frame=cap.read()
          cv2.imshow('video capture',frame)
          k=cv2.waitKey(30)
          if k & 0xFF ==ord('q'):
             break
cap.release()
cv2.destroyAllWindows()


     