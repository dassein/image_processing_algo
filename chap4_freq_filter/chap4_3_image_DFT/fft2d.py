# import cmath
import numpy as np 
from fft1d import fft, ifft # input, output are list

def pad2d(img): # img: narray
    H, W = img.shape[0], img.shape[1]
    s, t = 0, 0
    while 2**s < H:
        s += 1
    while 2**t < W:
        t += 1
    img_pad = np.pad(img, [(0, 2**s-H), (0, 2**t-W)], mode='constant')
    return img_pad


def fft2d(img):
    freq_spectrum = np.zeros_like(img, dtype=complex)
    M, N = img.shape[0], img.shape[1]
    for ii in range(M):
        freq_spectrum[ii, :] = fft(img[ii, :])
    for jj in range(N):
        freq_spectrum[:, jj] = fft(freq_spectrum[:, jj])
    return freq_spectrum


def ifft2d(freq_spectrum):
    img_conj = fft2d( np.conjugate(freq_spectrum) )
    return np.conjugate( img_conj ) / (freq_spectrum.shape[0] * freq_spectrum.shape[1])

norm = lambda x: np.absolute(x)

def shift_freq_center(freq_spectrum):
    H, W = freq_spectrum.shape[0], freq_spectrum.shape[1]
    tmp = np.zeros_like(freq_spectrum)
    freq_center = np.zeros_like(freq_spectrum)
    # for i in range(H):
    #     for j in range(W):
    #         index = (int(W/2) + j) % W
    #         tmp[i, index] = fft[i, j]
    # for j in range(W):
    #     for i in range(H):
    #         index = (int(H/2) + i) % H
    #         freq_center[index, j] = tmp[i, j]
    freq_center[:int(H/2), :int(W/2)] = freq_spectrum[int(H/2):, int(W/2):]
    freq_center[int(H/2):, int(W/2):] = freq_spectrum[:int(H/2), :int(W/2)]
    freq_center[:int(H/2), int(W/2):] = freq_spectrum[int(H/2):, :int(W/2)]
    freq_center[int(H/2):, :int(W/2)] = freq_spectrum[:int(H/2), int(W/2):]
    return freq_center


if __name__ == "__main__":
    sample = np.ones((3, 5))
    sample_pad = pad2d(sample)
    print(sample_pad[:, 1])

    import cv2
    import matplotlib.pyplot as plt
    img_gray = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
    img_pad = pad2d(img_gray[:, 0:512])
    freq_spectrum = fft2d(img_pad)
    log_norm_freq = 20 * np.log( norm(freq_spectrum) + 1 )
    cv2.imwrite('./output_images/chap4_3_freq.jpg', log_norm_freq)
    plt.imshow(log_norm_freq, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap4_3_freq_plt.jpg') # not grayscale
    plt.close()

    freq_center = shift_freq_center(freq_spectrum)
    log_norm_freq_center = 20 * np.log( norm(freq_center) + 1 )
    cv2.imwrite('./output_images/chap4_3_freq_center.jpg', log_norm_freq_center)
    plt.imshow(log_norm_freq_center, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap4_3_freq_center_plt.jpg') # not grayscale
    plt.close()

    img_recover = ifft2d(freq_spectrum)
    img_re = np.floor( norm(img_recover) ).astype(int)
    cv2.imwrite('./output_images/chap4_3_fft2d_recover.jpg', img_re)
    plt.imshow(img_re, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap4_3_fft2d_recover_plt.jpg') # not grayscale
    plt.close()
