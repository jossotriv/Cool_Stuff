from math import e, pi, sin, cos
j = 1j

from image import Image

import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fft2, ifft2, ifftshift, fftshift

# helper to normalize arrays so that the largest value has magnitude 1, useful
# for comparing images.
def normalize_1(x):
    return x / numpy.max(abs(x))

# define center_origin and uncenter_origin as we have done before.
center_origin = fftshift
uncenter_origin = ifftshift

# load the bluegill and the kernel
bluegill = Image.from_file('bluegill.png').to_array()
kernel = uncenter_origin(Image.from_file('kernel.png').to_array())

convolved = normalize_1(ifft2(fft2(bluegill) * fft2(kernel)))
