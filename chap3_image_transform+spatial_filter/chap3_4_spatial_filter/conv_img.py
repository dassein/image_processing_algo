import numpy as np 

def conv_img(img, filter): # img, filter are numpy arrays
    H, W = img.shape[0], img.shape[1]
    h_filter, w_filter = filter.shape[0], filter.shape[1]
    H_out, W_out = H - h_filter + 1, W - w_filter + 1
    img_conv = np.zeros((H_out, W_out))
    # for ii in range(H_out):
    #     for jj in range(W_out):
    #         img_conv[ii, jj] = np.sum(filter * img[ii:ii+h_filter, jj:jj+w_filter], axis=None)
    for i in range(h_filter):
        for j in range(w_filter):
            img_conv += filter[i, j] * img[i:i+H_out, j:j+W_out]
    return img_conv


if __name__ == "__main__":
    import cv2
    from matplotlib import pyplot as plt
    img_gray = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
    gauss_filter = np.asarray([[0, 1, 2, 1, 0],
                                [1, 3, 5, 3, 1],
                                [2, 5, 9, 5, 2],
                                [1, 3, 5, 3, 1],
                                [0, 1, 2, 1, 0]])
    gauss_filter = gauss_filter / np.sum(gauss_filter, axis=None)
    img_conv = conv_img(img_gray, gauss_filter)
    cv2.imwrite('./output_images/chap3_4_conv_img.jpg', img_conv)
    plt.imshow(img_conv, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap3_4_conv_img_plt.jpg') # not grayscale
    plt.close()
