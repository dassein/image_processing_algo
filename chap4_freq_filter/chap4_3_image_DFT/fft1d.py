import cmath
# import numpy
# import random

def memoize(f):
   cache = {}
   def memoizedFunction(*args):
      if args not in cache:
         cache[args] = f(*args)
      return cache[args]
   memoizedFunction.cache = cache
   return memoizedFunction

@memoize
def omega(p, q):
   return cmath.exp((2.0 * cmath.pi * 1j * q) / p)  # exp( 2pi * j * (q/p) )

def pad(inputList):
   k = 0
   while 2**k < len(inputList):
      k += 1
   return inputList + [0] * (2**k - len(inputList))

def fft(signal):  # len(signal) == 2**k
   n = len(signal)
   if n == 1:
      return signal
   else:
      Feven = fft([signal[i] for i in range(0, n, 2)])
      Fodd = fft([signal[i] for i in range(1, n, 2)])
      combined = [0] * n
      for m in range( int(n/2) ):
         combined[m] = Feven[m] + omega(n, -m) * Fodd[m]
         combined[m + int(n/2) ] = Feven[m] - omega(n, -m) * Fodd[m]
      return combined

def ifft(signal):
   timeSignal = fft([x.conjugate() for x in signal])
   return [x.conjugate()/len(signal) for x in timeSignal]

norm = lambda x: cmath.polar(x)[0]
# delta = [1, 0, 0, 0, 0, 0, 0, 0] # unshifted delta of length 8
# deltaShift = [0, 1, 0, 0, 0, 0, 0, 0] # unshifted delta of length 8

if __name__ == "__main__":
    # signal = [1, 0, 0, 1, 0, 0, 0]
    signal = [ cmath.exp(2.0 * cmath.pi * 1j * i *(5/8)) for i in range(5) ]
    signal_pad = pad(signal)
    freq_spectrum = fft(signal_pad)
    import matplotlib.pyplot as plt
    norm_freq = list( map(lambda x: norm(x), freq_spectrum) )
    # plt.bar( [i for i in range(len(freq_spectrum)) ], norm_freq )
    plt.stem(norm_freq, use_line_collection=True)
    plt.show()
    plt.savefig('./output_images/chap4_1_fft1d_plt.jpg')
    plt.close()

    signal_recover = ifft(freq_spectrum)
    print("singnal:"), print(signal)
    print("singnal_recover:"), print(signal_recover)
    norm_signal_re = list( map(lambda x: norm(x), signal_recover) )
    plt.stem(norm_signal_re, use_line_collection=True)
    plt.show()
    plt.savefig('./output_images/chap4_1_fft1d_re_plt.jpg')
    plt.close()
