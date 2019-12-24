# laplacian of guassian: LOG
import numpy as np 
from conv_img import conv_img

def LOG(img):
    filter_LOG = np.array([[-2, -4, -4, -4, -2],
                        [-4, 0, 8, 0, -4],
                        [-8, 8, 24, 8, -4],
                        [-4, 0, 8, 0, -4],
                        [-2, -4, -4, -4, -2]])
    img_conv = conv_img(img, filter_LOG)
    abs_img = np.abs( img_conv / np.sum(filter_LOG[filter_LOG > 0]) )
    img_out = np.floor(abs_img).astype(int)
    return img_out

if __name__ == "__main__":
    import cv2
    from matplotlib import pyplot as plt
    img_gray = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
    img_LOG = LOG(img_gray)
    cv2.imwrite('./output_images/chap3_4_LOG.jpg', img_LOG)
    plt.imshow(img_LOG, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap3_4_LOG_plt.jpg') # not grayscale
    plt.close()