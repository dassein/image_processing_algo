import numpy as np 
import cv2
import matplotlib
from matplotlib import pyplot as plt 

img_gray = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
# print(img_gray.shape)
img_contrast = np.zeros((img_gray.shape[0], img_gray.shape[1]))
mask1 = (img_gray < 256*3/8)
mask2 = (img_gray >= 256*5/8)
mask3 = (img_gray >= 256*3/8) * (img_gray < 256*5/8)
img_contrast[mask1] = img_gray[mask1]/3
img_contrast[mask2] = 256 - (256-img_gray[mask2])/3
img_contrast[mask3] = 256/2 + 3*(img_gray[mask3]-256/2)
img_contrast = ( np.floor(img_contrast) ).astype(int)
cv2.imwrite('./output_images/chap3_2_contrast.jpg', img_contrast)
# print(img_contrast)
plt.imshow(img_contrast, cmap='gray') # show in gray scale
plt.show(block=False)
plt.savefig('./output_images/chap3_2_contrast_plt.jpg') # not grayscale