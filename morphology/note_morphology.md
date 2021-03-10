reference: https://zhuanlan.zhihu.com/p/67566843

A - binary image, B - Structuring element (kernel)  
B usually is filled with all 1
### Dilation
$$
A \oplus B=\bigcup_{b \in B} A_{b}
$$
where $A_b$ is the translation of A by b.  


### Erosion
$$
A \ominus B=\bigcap_{b \in B} A_{-b}
$$
where $A_b$ denotes the translation of A by -b  
注意：在腐蚀中平移的方向和膨胀时相反，最后是取交集

### Opening
$$
A \circ B=(A \ominus B) \oplus B
$$

usage: remove the outlier/small objects whose size < B (morphological noise removal)  
usage: B水平长条的矩形，提取水平线；B竖直长条的矩形，提取竖直线  
see `open_extract_line.cpp`

### Closing
$$
A \bullet B=(A \oplus B) \ominus B
$$

usage: removes small holes whose size < B


### Morphological Gradient
$$
(A \oplus B) - (A \ominus B)
$$
usage: 突出团块（blob）的边缘, 保留物体的边缘轮廓

### Top Hat
$$
T_{w}(A)=A - A \circ B
$$
where $\circ$ denotes the opening operation  
usage: 提取 背景with small objects (开运算: 放大裂缝/消除 small object)

### Black Hat (Bottom Hat)
$$
T_{b}(A)=A \bullet B - A
$$
where $\bullet$ is the closing operation  
usage: 提取 背景with small holes (闭运算: 消除 small holes)

### Hit and Miss transform
reference: https://zhuanlan.zhihu.com/p/67566843  
reference: https://en.wikipedia.org/wiki/Hit-or-miss_transform  
usage: 从图像中求取特殊的特征 (先在前景获取特征，然后在背景中剔除特)  
特殊特征：
* isolated pixels，孤立像素
* end points，顶点
* contour points，轮廓边缘点
