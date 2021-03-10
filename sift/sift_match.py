'''
Brute-Force Matcher with SIFT descriptor
https://docs.opencv.org/master/dc/dc3/tutorial_py_matcher.html

note:
The result of matches = bf.match(des1,des2) line is a list of DMatch objects. This DMatch object has following attributes:
    DMatch.distance - Distance between descriptors. The lower, the better it is.
    DMatch.trainIdx - Index of the descriptor in train descriptors
    DMatch.queryIdx - Index of the descriptor in query descriptors
    DMatch.imgIdx - Index of the train image.
'''
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img1 = cv.imread('./bin/sift_match_1.png',cv.IMREAD_GRAYSCALE)          # queryImage
img2 = cv.imread('./bin/sift_match_2.png',cv.IMREAD_GRAYSCALE) # trainImage
# Initiate SIFT detector
num_keypoint = 300 # number of key points
sift = cv.SIFT_create(num_keypoint)                                                                                 
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2) # use BFMatcher.knnMatch() to get k best matches
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance: # 1st match < ratio * 2nd match 
        good.append([m])
# cv.drawMatchesKnn expects list of lists as matches.
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv.imwrite('./bin/sift_match.png',img3)
plt.imshow(img3)
plt.show()