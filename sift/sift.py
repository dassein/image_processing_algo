import numpy as np
import cv2 as cv
img = cv.imread('./bin/sift_match_1.png')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
num_keypoint = 100 # number of key points
sift = cv.SIFT_create(num_keypoint)
kp = sift.detect(gray,None)
img=cv.drawKeypoints(gray,kp,img)
cv.imwrite('./bin/sift_match_1+keypoint.png',img)