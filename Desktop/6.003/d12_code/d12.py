import numpy
from numpy.fft import fft2, ifft2, fftshift, ifftshift

from PIL import Image

center_origin=fftshift
uncenter_origin=ifftshift

def pad(array, r_pad=1, c_pad=1, mode='extend'):
    """
    Given a numpy array, make a larger array by "padding" the edges of the
    array (adding r_pad number of pixels to the top and bottom of the array,
    and c_pad number of pixels to the left and right of the array).

    If mode is 'extend', then the values on the edge of the array are repeated
    in the padded region.  If mode is 'zero', then the array will instead be
    padded by zeros.
    """
    if mode == 'extend':
        _nmode = 'edge'
    elif mode == 'zero':
        _nmode = 'constant'
    else:
        raise ValueError('Invalid mode for pad: %s' % mode)
    return numpy.pad(array, ((r_pad, r_pad), (c_pad, c_pad)), _nmode)


def png_to_array(fname):
    """
    Load the PNG image with the given filename into a numpy array.
    """
    with Image.open(fname) as image:
        im_arr = numpy.fromstring(image.convert('L').tobytes(), dtype=numpy.uint8)
        im_arr = im_arr.reshape((image.size[1], image.size[0]))
    return im_arr.astype(numpy.float64)/255


def array_to_png(arr, fname):
    h = len(arr)
    w = len(arr[0])
    out = Image.new(mode='L', size=(w, h))
    out.putdata(numpy.around(255*arr).reshape(w*h))
    out.save(fname)


