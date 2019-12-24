import numpy as np 
from conv_img import conv_img

def regularize(img):
    img_out = ( np.floor(img) ).astype(int)
    mask1 = (img_out > 255)
    mask2 = (img_out < 0)
    img[mask1] = 255
    img[mask2] = 0
    return img_out
    
def laplace(img, alpha=0.4):
    filter_laplace = np.array([[-1, -1, -1],
                            [-1, 8, -1],
                            [-1, -1, -1]])
    img_conv = conv_img(img, filter_laplace)
    # abs_img = np.abs(img_conv)
    img_nopad = img_conv / np.max(filter_laplace)
    img_pad = np.pad(img_nopad, [(1, 1), (1, 1)], mode='constant')  # 2*pad = 2*1 = (h of filter - 1) = 3-1
    return regularize( alpha * img_pad + img )

if __name__ == "__main__":
    import cv2
    from matplotlib import pyplot as plt
    img_gray = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
    img_laplace = laplace(img_gray)
    cv2.imwrite('./output_images/chap3_4_laplace.jpg', img_laplace)
    plt.imshow(img_laplace, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap3_4_laplace_plt.jpg') # not grayscale
    plt.close()

    
