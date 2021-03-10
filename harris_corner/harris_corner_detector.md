## harris corner dectctor

reference: https://en.wikipedia.org/wiki/Spatial_gradient  
reference: https://en.wikipedia.org/wiki/Sobel_operator  
reference: https://docs.opencv.org/master/dc/d0d/tutorial_py_features_harris.html  
reference: http://www.cs.cornell.edu/courses/cs4670/2015sp/lectures/lec07_harris_web.pdf  
reference: https://github.com/ShivamChourey/Harris-Corner-Detection/blob/master/Corner_Detection.py  
reference: https://medium.com/pixel-wise/detect-those-corners-aba0f034078b

[toc]

### RGB -> Intensity
$$
I = \sum_{C \in\{R, B, G\}} w_{C} \cdot C
$$
where $w_{R}=0.299, w_{B}=0.587, w_{G}=1-\left(w_{R}+w_{B}\right)$

### Spatial derivative

We compute derivatives with **Sobel** operator
$$
I_x = \frac{\partial I}{\partial x} \approx 
\left[\begin{array}{lll}
+1 & 0 & -1 \\
+2 & 0 & -2 \\
+1 & 0 & -1
\end{array}\right] * I
= \left[\begin{array}{l}
1 \\2 \\1
\end{array}\right] *\left(\left[\begin{array}{lll}
+1 & 0 & -1
\end{array}\right] * I\right)
$$

$$
I_y = \frac{\partial I}{\partial y} \approx 
\left[\begin{array}{ccc}
+1 & +2 & +1 \\
0 & 0 & 0 \\
-1 & -2 & -1
\end{array}\right] * I
= \left[\begin{array}{c}
+1 \\0 \\-1
\end{array}\right] *\left(\left[\begin{array}{lll}
1 & 2 & 1
\end{array}\right] * I\right)\\
$$



note: convolution = 1. flip kernel, 2. correlation with the flipped kernel  
note: we use $[1\ 2\ 1]$ to smoothen the operator $\frac{\partial}{\partial x},\frac{\partial}{\partial y}$ in direction of $y, x$

### Consider the Intensity deviation
$$
(\mathrm{d} I)^2 = 
\left[I(x+\mathrm{d}x, y+\mathrm{d}y)-I(x, y)\right]^2
\approx  \begin{bmatrix}\mathrm{d}x\\ \mathrm{d}y\end{bmatrix}^T
\left[\begin{array}{cc}
I_{x}^{2} & I_{x} I_{y} \\
I_{x} I_{y} & I_{y}^{2}
\end{array}\right]
\begin{bmatrix}\mathrm{d}x\\ \mathrm{d}y\end{bmatrix}
$$
note: Harris corner detector 旋转不变性，不具有尺度不变性 (尺度变化 -> 角点变为边缘)  
Corner location is covariant w.r.t. rotation  
Corner location is not covariant to scaling  
To obtain better estimation for the inner matrix, we can apply **Gaussian** filter $w$ to the matrix
$$
M=\sum_{x, y} w(x, y)\left[\begin{array}{ll}
I_{x}^2 & I_{x} I_{y} \\
I_{x} I_{y} & I_{y}^2
\end{array}\right]
= \left[\begin{array}{ll}
w * I_{x}^2 & w * [I_{x} I_{y}] \\
w * [I_{x} I_{y}] & w * [I_{y}^2]
\end{array}\right]
= \left[\begin{array}{ll}
A & B \\
B & C
\end{array}\right]
$$

where 
$$
w * \text{image} \equiv \left[\begin{array}{lll}
1 & 2 & 1 \\
2 & 4 & 2 \\
1 & 2 & 1
\end{array}\right] * \text{image}
= \left[\begin{array}{l}
1 \\2 \\1
\end{array}\right] *\left(\left[\begin{array}{lll}
1 & 2 & 1
\end{array}\right] * \text{image}\right)
$$

Finally, for each pixel $(x, y)$, we have a corresponding 2 by 2 matrix $M$  
$$
(\mathrm{d} I)^2 \approx 
\begin{bmatrix}\mathrm{d}x\\ \mathrm{d}y\end{bmatrix}^T
M
\begin{bmatrix}\mathrm{d}x\\ \mathrm{d}y\end{bmatrix}
$$

Think about the contour around $(x, y)$ where $(\mathrm{d} I)^2=\text{const}$, here we assume $\text{const}=1$

>Proposition.  
ellipse equation $A\mathrm{d}x^2 + 2B\mathrm{d}x\mathrm{d}y + C\mathrm{d}y^2 = 1$,   
suppose its semi-major axis and semi-minor axis are respectively $a,b$，  
thus eigenvalues of $M$ are $\lambda= \frac{1}{a^2}, \frac{1}{b^2}$  
Proof:  
find the shortest or longest distance $d^2 = \mathrm{d}x^2 + \mathrm{d}y^2$ on the ellipse  
set Lagrangian $L= (\mathrm{d}x^2 + \mathrm{d}y^2) + \frac{1}{\lambda}\left[A\mathrm{d}x^2 + 2B\mathrm{d}x\mathrm{d}y + C\mathrm{d}y^2 - 1\right]$  
$L_x=0,L_y=0$ lead to $\text{det}(\lambda I - M)=0$,  
and $(\mathrm{d}x^2 + \mathrm{d}y^2)=\frac{1}{\lambda} \left[A\mathrm{d}x^2 + 2B\mathrm{d}x\mathrm{d}y + C\mathrm{d}y^2\right]=\frac{1}{\lambda}$  
Thus we know $\frac{1}{\lambda}=a^2, b^2$

With the preposition, we know that
* smooth region at (x, y):  
  -> Intensity changes slowly for all directions  
  -> $a, b$ are big  
  -> both eigenvalues $\lambda$ are small
* edge at (x, y):  
  -> Intesity changes fast in one direction  
  -> $b$ is small, $a$ is big  
  -> $\lambda_2$ is big, $\lambda_1$ is small
* corner at (x, y):  
  -> Intesity changes fast in 2 directions  
  -> both $a, b$ are small  
  -> both eigenvalues $\lambda$ are big

### 1. Harris response
define **Harris Response** as follows to determine whether both $\lambda$ are big

$$
R=\lambda_{1} \lambda_{2}-k \cdot\left(\lambda_{1}+\lambda_{2}\right)^{2}=\operatorname{det}(M)-k \cdot \operatorname{tr}(M)^{2}
$$
where $k \in[0.04,0.06]$  
usage: opencv python  `cv2.cornerHarris(src, blockSize, ksize, k[, dst[, borderType]])`
```python
# src - 输入灰度图像，float32类型
# blockSize - 用于角点检测的邻域大小，就是上面提到的窗口(eg. gaussian filter)的尺寸
# ksize - 用于计算梯度图的Sobel算子的尺寸
# k - 用于计算角点响应函数的参数k，取值范围常在0.04~0.06之间
import cv2 as cv
import numpy as np

# detector parameters
block_size = 5
sobel_size = 3
k = 0.04

image = cv2.imread('bird.jpg')
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# modify the data type setting to 32-bit floating point 
gray_img = np.float32(gray_img)
# detect the corners with appropriate values as input parameters
corners_img = cv2.cornerHarris(gray_img, block_size, sobel_size, k)
# result is dilated for marking the corners, not necessary
dst = cv.dilate(corners_img, None)
# Threshold for an optimal value, marking the corners in Green
image[corners_img>0.01*corners_img.max()] = [0,0,255]
cv2.imwrite('new_bird.jpg', image)
```


### 2. Shi-Tomasi
deffine the determinant as follow
$$
R =\min \left(\lambda_{1}, \lambda_{2}\right)
$$

If $R$ is greater than a threshold, its classified as a corner  
usage: opencv python `goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]])`  
explantion: 
1. 低于质量水平的角点都会被忽略
2. 把合格角点按角点质量进行降序排列
3. 保留质量最高的一个角点
4. 将它附近（最小距离之内）的角点都删掉（类似于非极大值抑制）
5. 按这样的方式最后得到 N 个最佳角点
```python
# image：输入灰度图像，float32类型
# maxCorners：返回角点的最大数目，值为0表表示没有设置最大值限制，返回所有检测到的角点。
# qualityLevel：质量系数（小于1.0的正数，一般在0.01-0.1之间），表示可接受角点的最低质量水平。该系数乘以最好的角点分数（也就是上面较小的那个特征值），作为可接受的最小分数；例如，如果最好的角点分数值为1500且质量系数为0.01，那么所有质量分数小于15的角都将被忽略。
# minDistance：角之间最小欧式距离，忽略小于此距离的点。
# corners：输出角点坐标mask：可选的感兴趣区域，指定想要检测角点的区域。blockSize：默认为3，角点检测的邻域大小（窗口尺寸）
# useHarrisDetector：用于指定角点检测的方法，如果是true则使用Harris角点检测，false则使用Shi Tomasi算法。默认为False。
# k：默认为0.04，Harris角点检测时使用
import numpy as np
import cv2

maxCorners = 100
qualityLevel = 0.01
minDistance = 10

img = cv2.imread('bird.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, maxCorners, qualityLevel, minDistance)

corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),2,(0,0,255),-1)
    
cv2.imwrite('new_bird.jpg', img)
```
