import numpy
from numpy.fft import fft2, ifft2, fftshift, ifftshift
from image import Image


def center_origin(array):
    """
    Given a numpy array whose (0,0) point is in the top-left corner, return a
    new numpy array whose (0,0) point is in the center of the array.
    """
    return fftshift(array)


def uncenter_origin(array):
    """
    Given a numpy array whose (0,0) point is in the center of the array, return
    a new numpy array whose (0,0) point is in the top-left corner.
    """
    return ifftshift(array)


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


def unpad(array, r_pad=1, c_pad=1):
    """
    An inverse operation to pad.  Removes edges that were added by padding.
    """
    assert r_pad != 0 and c_pad != 0, "Padding values must be nonzero"
    return array[r_pad:-r_pad, c_pad:-c_pad]


def convolve_2d_fft(image, kernel, pad_edges=True):
    """
    Convolve `image` (an instance of `Image`, origin in the upper left) with
    `kernel` (a numpy array, origin in the center of the array) by operating in
    the frequency domain.

    If pad_edges is True, first pad the edges of the image (in 'extend' mode)
    and unpad at the end.  Otherwise, do not pad the image at all (in this
    case, boundary effects may be seen).

    Return a numpy array containing the result of the convolution.
    """
    raise NotImplementedError
