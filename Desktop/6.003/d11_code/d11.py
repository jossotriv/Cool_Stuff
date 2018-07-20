from math import e, pi, sin, cos
j = 1j

from image import Image
from wav_utils import Wave

import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fft2, ifft2

def convolve_causal(x, y):
    out = [0] * (len(x)+len(y))
    for i in range(len(x)):
        for j in range(len(y)):
            out[i+j] += y[j] * x[i]
    return out
