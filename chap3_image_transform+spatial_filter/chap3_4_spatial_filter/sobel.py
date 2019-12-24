import numpy as np 
from conv_img import conv_img

def sobel(img):
    filter_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    filter_y = np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]])
    img_x = conv_img(img, filter_x)
    img_y = conv_img(img, filter_y)
    sq_img = np.sqrt(img_x**2 + img_y**2)
    img_out = np.floor(sq_img * (256 / np.max(sq_img)))
    return img_out

if __name__ == "__main__":
    import cv2
    from matplotlib import pyplot as plt
    img_gray = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
    img_sobel = sobel(img_gray)
    cv2.imwrite('./output_images/chap3_4_sobel.jpg', img_sobel)
    plt.imshow(img_sobel, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap3_4_sobel_plt.jpg') # not grayscale
    plt.close()

    
