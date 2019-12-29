import numpy as np 

gauss = lambda i, j, D0: np.exp(-( i**2+j**2 ) / (2*D0**2) )

def filter_gauss_init(H, W, D0):
    freq_filter = [ [ gauss(i, j, D0) for j in range(W)] for i in range(H) ]
    return np.array(freq_filter)

if __name__ == "__main__":
    import matplotlib.pyplot as plt 
    from dct2d import dct2d, idct2d, pad2d
    import cv2
    img_gray = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
    img_pad = pad2d(img_gray[:, 0:512])
    freq_spectrum = dct2d(img_pad)
    f_gauss = filter_gauss_init(img_pad.shape[0], img_pad.shape[0], min(img_pad.shape) / 2) 
    # fft(N, freq:0-2pi=>0-N): D0=min/4 <=> dct(2N, freq:0-pi=>0-N): D0=min/2
    plt.imshow(f_gauss, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap4_x_filter_dct_gauss_plt.jpg')
    plt.close()

    freq_filtered = freq_spectrum * f_gauss

    img_recover = idct2d(freq_filtered)
    img_re = np.floor( img_recover ).astype(int)
    cv2.imwrite('./output_images/chap4_x_freq_filter_dct_recover.jpg', img_re)
    plt.imshow(img_re, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap4_x_freq_filter_dct_recover_plt.jpg') 
    plt.close()
