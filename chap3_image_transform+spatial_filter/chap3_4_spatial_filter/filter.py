import numpy as np 
from conv_img import conv_img

def filter_gauss(img):
    gauss_filter = np.asarray([[0, 1, 2, 1, 0],
                                [1, 3, 5, 3, 1],
                                [2, 5, 9, 5, 2],
                                [1, 3, 5, 3, 1],
                                [0, 1, 2, 1, 0]])
    gauss_filter = gauss_filter / np.sum(gauss_filter, axis=None)
    img_conv = conv_img(img, gauss_filter)
    return img_conv

def filter_laplace(img):
    laplace_filter = (1.0/16) * np.array(
                    [[0, 0, -1, 0, 0],
                    [0, -1, -2, -1, 0],
                    [-1, -2, 16, -2, -1],
                    [0, -1, -2, -1, 0],
                    [0, 0, -1, 0, 0]])
    img_conv = conv_img(img, laplace_filter)
    return img_conv

def filter_box(img):
    box_filter = np.ones((7, 7)) / (7 * 7)
    img_conv = conv_img(img, box_filter)
    return img_conv

def filter_max(img, h_filter=7, w_filter=7):
    H, W = img.shape[0], img.shape[1]
    # h_filter, w_filter = filter.shape[0], filter.shape[1]
    H_out, W_out = H - h_filter + 1, W - w_filter + 1
    img_conv = np.zeros((H_out, W_out))
    for ii in range(H_out):
        for jj in range(W_out):
            img_conv[ii, jj] = np.max(img[ii:ii+h_filter, jj:jj+w_filter], axis=None)
    return img_conv

def filter_median(img, h_filter=7, w_filter=7):
    H, W = img.shape[0], img.shape[1]
    # h_filter, w_filter = filter.shape[0], filter.shape[1]
    H_out, W_out = H - h_filter + 1, W - w_filter + 1
    img_conv = np.zeros((H_out, W_out))
    for ii in range(H_out):
        for jj in range(W_out):
            img_conv[ii, jj] = np.median(img[ii:ii+h_filter, jj:jj+w_filter], axis=None)
    return img_conv


def weighted_median(data, weights):
    """
    Args:
      data (list or numpy.array): data
      weights (list or numpy.array): weights
    """
    data, weights = np.array(data).ravel(), np.array(weights).ravel()
    s_data, s_weights = map(np.array, zip(*sorted(zip(data, weights))))
    midpoint = 0.5 * sum(s_weights)
    if any(weights > midpoint):
        w_median = (data[weights == np.max(weights)])[0]
    else:
        cs_weights = np.cumsum(s_weights)
        idx = np.where(cs_weights <= midpoint)[0][-1]
        if cs_weights[idx] == midpoint:
            w_median = np.mean(s_data[idx:idx+2])
        else:
            w_median = s_data[idx+1]
    return w_median


def filter_weighted_median(img):
    weight = np.array([[0, 0, 1, 2, 1, 0, 0],
                        [0, 1, 2, 3, 2, 1, 0],
                        [1, 2, 3, 4, 3, 2, 1],
                        [2, 3, 4, 5, 4, 3, 2],
                        [1, 2, 3, 4, 3, 2, 1],
                        [0, 1, 2, 3, 2, 1, 0],
                        [0, 0, 1, 2, 1, 0, 0]])
    H, W = img.shape[0], img.shape[1]
    h_weight, w_weight = weight.shape[0], weight.shape[1]
    H_out, W_out = H - h_weight + 1, W - w_weight + 1
    img_conv = np.zeros((H_out, W_out))
    for ii in range(H_out):
        for jj in range(W_out):
            img_conv[ii, jj] = weighted_median(img[ii:ii+h_weight, jj:jj+w_weight], weight)
    return img_conv

if __name__ == "__main__":
    import cv2
    from matplotlib import pyplot as plt
    img_gray = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
    img_gauss = filter_gauss(img_gray)
    cv2.imwrite('./output_images/chap3_4_filter_gauss.jpg', img_gauss)
    plt.imshow(img_gauss, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap3_4_filter_gauss_plt.jpg') # not grayscale
    plt.close()

    img_laplace = filter_laplace(img_gray)
    cv2.imwrite('./output_images/chap3_4_filter_laplace.jpg', img_laplace)
    plt.imshow(img_laplace, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap3_4_filter_laplace_plt.jpg') # not grayscale
    plt.close()

    img_box = filter_box(img_gray)
    cv2.imwrite('./output_images/chap3_4_filter_box.jpg', img_box)
    plt.imshow(img_box, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap3_4_filter_box_plt.jpg') # not grayscale
    plt.close()

    img_max = filter_max(img_gray)
    cv2.imwrite('./output_images/chap3_4_filter_max.jpg', img_max)
    plt.imshow(img_max, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap3_4_filter_max_plt.jpg') # not grayscale
    plt.close()

    img_median = filter_median(img_gray)
    cv2.imwrite('./output_images/chap3_4_filter_median.jpg', img_median)
    plt.imshow(img_median, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap3_4_filter_median_plt.jpg') # not grayscale
    plt.close()

    img_weighted_median = filter_weighted_median(img_gray)
    cv2.imwrite('./output_images/chap3_4_filter_weighted_median.jpg', img_weighted_median)
    plt.imshow(img_weighted_median, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap3_4_filter_weighted_median_plt.jpg') # not grayscale
    plt.close()