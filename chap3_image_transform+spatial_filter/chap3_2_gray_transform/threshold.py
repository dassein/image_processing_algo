import numpy as n 
import cv2
import matplotlib
from matplotlib import pyplot as plt 

threshold = 150
img_gray = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)

img_binarized = 255 * (img_gray > threshold)
cv2.imwrite('./output_images/chap3_2_threshold.jpg', img_binarized)

# [b, g, r] = cv2.split(img_binarized)
# img_binarized_plt = cv2.merge([r, g, b])
# del r, g, b, img_binarized, img_gray
plt.imshow(img_binarized, cmap='gray') # show in gray scale
# more colormap, see: https://scipy-cookbook.readthedocs.io/items/Matplotlib_Show_colormaps.html
plt.show(block=False)
plt.savefig('./output_images/chap3_2_threshold_plt.jpg') # not grayscale