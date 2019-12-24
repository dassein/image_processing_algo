import numpy as np 

gauss = lambda i, j, H, W, D0: np.exp(-( (i-int(H/2))**2+(j-int(W/2))**2 ) / (2*D0**2) )

def filter_gauss_init(H, W, D0):
    freq_filter = [ [ gauss(i, j, H, W, D0) for j in range(W)] for i in range(H) ]
    return np.array(freq_filter)

if __name__ == "__main__":
    import matplotlib.pyplot as plt 
    

    import cv2
    from fft2d import fft2d, ifft2d, pad2d, shift_freq_center, norm
    img_gray = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
    img_pad = pad2d(img_gray[:, 0:512])
    freq_spectrum = fft2d(img_pad)
    freq_center = shift_freq_center(freq_spectrum) # left up corner => center
    f_gauss = filter_gauss_init(img_pad.shape[0], img_pad.shape[0], min(img_pad.shape) / 4)
    plt.imshow(f_gauss, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap4_3_filter_gauss_plt.jpg')
    plt.close()

    freq_center_filtered = freq_center * f_gauss
    freq_filtered = shift_freq_center( freq_center_filtered ) # center => left up corner

    img_recover = ifft2d(freq_filtered)
    img_re = np.floor( norm(img_recover) ).astype(int)
    cv2.imwrite('./output_images/chap4_3_freq_filter_recover.jpg', img_re)
    plt.imshow(img_re, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap4_3_freq_filter_recover_plt.jpg') 
    plt.close()
