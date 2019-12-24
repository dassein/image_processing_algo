import numpy as np 
import cv2 
import matplotlib
from matplotlib import pyplot as plt 

img_gray = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
# print(img_gray.shape)
# img_contrast = np.zeros((img_gray.shape[0], img_gray.shape[1]))
MAX, MIN = img_gray.max(), img_gray.min()
epsilon = 1e-6
img_contrast = 256 * (img_gray - MIN) / (MAX - MIN + epsilon)
img_contrast = ( np.floor(img_contrast) ).astype(int)
cv2.imwrite('./output_images/chap3_2_auto_contrast.jpg', img_contrast)
# print(img_contrast)
plt.imshow(img_contrast, cmap='gray') # show in gray scale
plt.show(block=False)
plt.savefig('./output_images/chap3_2_auto_contrast_plt.jpg') # not grayscale