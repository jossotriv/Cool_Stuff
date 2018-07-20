from wav_utils import Wave
from numpy.fft import fft,ifft,fftshift,ifftshift
from matplotlib import pyplot
from math import e, pi, sin, cos, log
j = complex(0,1)

def hann(n,N):
    return sin(pi*n/(N-1))**2
