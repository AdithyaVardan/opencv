import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
#cv.imshow('blank',blank)
#paint the image certain colors and
#blank[200:300,300:400]=0,255,0
#cv.imshow('blank1',blank)
#rectangle 
cv.rectangle(blank,(0,0),(220,500),(0,0,255),thickness=2)
cv.imshow('blank',blank)
cv.waitKey(0)