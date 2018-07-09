import cv2
import numpy as np
import random as rd
from math import floor
original = cv2.imread('guitar.jpg')

cv2.imshow('hello world',original)


mod = original.copy()

for row in range(mod.shape[0]):
     temp=row*rd.random()+1
     for column in range(mod.shape[1]):
           if row%2==0 and column%temp==0:
              r=floor(rd.random()*255)
              g=floor(rd.random()*255)
              b=floor(rd.random()*255)
              mod[row,column]=(r,g,b)

cv2.imshow('hello world',mod)
cv2.waitKey(0)
cv2.destroyAllWindows()
