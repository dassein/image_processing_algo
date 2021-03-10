import numpy as np 
from dct1d import dct, idct

def pad2d(img): # img: narray
    H, W = img.shape[0], img.shape[1]
    s, t = 0, 0
    while 2**s < H:
        s += 1
    while 2**t < W:
        t += 1
    img_pad = np.pad(img, [(0, 2**s-H), (0, 2**t-W)], mode='constant')
    return img_pad

def dct2d(img_pad):   
    H, W = img_pad.shape[0], img_pad.shape[1]
    freq_spectrum = np.zeros((H, W), dtype=float)
    for ii in range(H): # you can do row then column; OR do column then row
        freq_spectrum[ii, :] = dct(img_pad[ii, :])
    for jj in range(W):
        freq_spectrum[:, jj] = dct(freq_spectrum[:, jj])
    return freq_spectrum

def idct2d(freq_spectrum):    
    H, W = freq_spectrum.shape[0], freq_spectrum.shape[1]
    img_recover = np.zeros((H, W), dtype=float)
    for jj in range(W):
        img_recover[:, jj] = idct(freq_spectrum[:, jj])
    for ii in range(H): # you can do row then column; OR do column then row
        img_recover[ii, :] = idct(img_recover[ii, :])

    return img_recover

norm = lambda x: np.absolute(x)

if __name__ == "__main__":
    sample = np.ones((3, 5))
    sample_pad = pad2d(sample)
    print(sample_pad[:, 1])

    import cv2
    import matplotlib.pyplot as plt
    img_gray = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
    img_pad = pad2d(img_gray[:, 0:512])
    freq_spectrum = dct2d(img_pad)
    log_norm_freq = 20 *np.log( norm(freq_spectrum) + 1 )
    cv2.imwrite('./output_images/chap4_x_dct2d_freq.jpg', log_norm_freq)
    plt.imshow(log_norm_freq, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap4_x_dct2d_freq_plt.jpg') # not grayscale
    plt.close()

    img_recover = idct2d(freq_spectrum)
    img_re = np.floor( img_recover ).astype(int)
    cv2.imwrite('./output_images/chap4_x_dct2d_recover.jpg', img_re)
    plt.imshow(img_re, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap4_x_dct2d_recover_plt.jpg') # not grayscale
    plt.close()
