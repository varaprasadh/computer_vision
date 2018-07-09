
import cv2
import numpy as np

cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier('facecascade.xml')

eye_cascade=cv2.CascadeClassifier('eyecascade.xml')

while True:
          ret,img=cap.read()
          gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
          faces=face_cascade.detectMultiScale(gray)
          for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
                r_gray=gray[y:y+h,x:x+w]
                r_color= img[y:y+h,x:x+w]
                eyes=eye_cascade.detectMultiScale(r_gray)
                for (ex,ey,ew,eh) in eyes:
                      cv2.rectangle(r_color,(ex,ey),(ex+ew,ey+eh),(0,255,100),2)
                      
          cv2.imshow('faces',img)
          k=cv2.waitKey(30)
          if k & 0xff== ord('q') :
             cv2.imwrite("snap.jpg",img)
             break
cap.release()
cv2.destroyAllWindows()


























