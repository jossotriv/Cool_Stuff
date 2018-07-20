import sys
dft_module = __import__('idft_compiled.idft_py%s' % ''.join(map(str, max(sys.version_info[:3], (3,5,0)))), fromlist=['idft2'])
globals().update({i: getattr(dft_module, i) for i in ('idft2',)})

from image import Image
from math import pi,e,cos,sin
from matplotlib import pyplot
j = complex(0,1)


def G(x0, y0, wx, wy, omega_x, omega_y):
    pass    # your code here


def MIT(omega_x, omega_y):
    pass    # your code here
