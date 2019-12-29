import numpy as np 
from fft1d import fft, ifft, pad, omega

def flip_expand(list_src):
    # Wrong:(when list_src is np array) return list_src + list( item for item in reversed(list_src) )
    return np.concatenate((list_src, list_src[-1::-1]))


norm = lambda x: np.absolute(x)

def sign(list_src):
    return 2 * ( np.real(list_src) >= 0) - 1  # real() >= 0: +1; real() < 0: -1

def dct(signal_pad):
    n = len(signal_pad)
    signal_expand = flip_expand( signal_pad ) # length: N->2N
    freq_spectrum_2N = fft(signal_expand)
    freq_spectrum_part1 = freq_spectrum_2N[:n]
    return sign(freq_spectrum_part1) * norm(freq_spectrum_part1) # only works for Real signal
    # return np.real( [ omega(4*n, -i)*freq_spectrum_part1[i] for i in range(n) ] )


def idct(freq_spectrum):  
    n = len(freq_spectrum)
    freq_factor = [ omega(4*n, i)*freq_spectrum[i] for i in range(n) ]
    freq_fft = freq_factor + [ 0 ] + list( np.conjugate(freq_factor[-1:0:-1]) )
    signal_fft = ifft(freq_fft)
    return np.real(signal_fft[:n])  # imginary part of signal_fft == 0 for Real signal

if __name__ == "__main__":
    import cmath
    import matplotlib.pyplot as plt
    # signal = [ np.cos(2.0 * np.pi * i *(5/8)) for i in range(8) ]
    signal = [5, -1, 3, 4, 5]
    signal_pad = pad( signal )
    signal_expand = flip_expand(signal_pad)
    plt.stem( signal_pad, use_line_collection=True)
    plt.show()
    plt.savefig('./output_images/chap4_x_dct1d_signal_plt.jpg')
    plt.close()

    signal_fft = fft(signal_expand)
    norm_freq = norm( signal_fft[:len(signal_pad)] ) * sign( signal_fft[:len(signal_pad)] )
    plt.stem(norm_freq, use_line_collection=True)
    plt.show()
    plt.savefig('./output_images/chap4_x_fft1d_plt.jpg')
    plt.close()

    dct_freq = dct(signal_pad)
    plt.stem(dct_freq, use_line_collection=True)
    plt.show()
    plt.savefig('./output_images/chap4_x_dct1d_plt.jpg')
    plt.close()

    dct_recover = idct(dct_freq)
    plt.stem(dct_recover, use_line_collection=True)
    plt.show()
    plt.savefig('./output_images/chap4_x_idct1d_plt.jpg')
    plt.close()