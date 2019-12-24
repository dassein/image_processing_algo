import numpy as np 
import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
img = cv2.imread('./images/low_contrast.jpg')
max_intensity = 255
img_invert = max_intensity - img
# print(img_invert)
cv2.imwrite('./output_images/chap3_2_invert.jpg', img_invert)
# 彩色图像使用OpenCV加载时是BGR模式。Matplotlib是RGB模式。所以如果彩色图像已经被OpenCV读取
# #method1
# b,g,r=cv2.split(img)
# img2=cv2.merge([r,g,b])
# plt.imshow(img2)
# plt.show()
# #method2
# img3=img[:,:,::-1]
# plt.imshow(img3)
# plt.show()
# #method3
# img4=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img4)
# plt.show()

[b, g, r] = cv2.split(img_invert)
img_invert_plt = cv2.merge([r, g, b])
plt.imshow(img_invert_plt)
plt.show(block=False)
plt.savefig('./output_images/chap3_2_invert_plt.jpg')  