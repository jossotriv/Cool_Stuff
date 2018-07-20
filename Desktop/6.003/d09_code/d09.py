import numpy
from numpy.fft import fft2, ifft2, fftshift, ifftshift
from image import Image


# filtering function (low-pass / high-pass
def filter(X, lo=True, x_om_c=0.05, y_om_c=None):
    """
    Given a numpy array containing DFT coefficients, where (Kx=0, Ky=0) is in
    the center of the array, return a filtered version of the DFT coefficients.

    If lo==True, we will keep only the low frequency content (i.e.,
    coefficients below the specified cutoff frequency); otherwise, we do the
    opposite.

    x_om_c is a cutoff, such that the actually frequency cutoff Omega_x is
    x_om_c times 2pi.

    y_om_c is the same, but in the y direction.  If y_om_c is not specified, it
    is assumed to be the same as x_om_c.
    """
    if y_om_c is None:
        y_om_c = x_om_c
    X2 = numpy.array(X)
    nr, nc = X2.shape
    xkc = round(x_om_c * nc)
    ykc = round(y_om_c * nr)
    for r in range(nr):
        for c in range(nc):
            keep = ((r-nr//2)**2/ykc**2 + (c-nc//2)**2/xkc**2) < 1
            if not lo:
                keep = not keep
            X2[r, c] *= keep
    return X2


def sample_gauss(x, sigma=1, mu=0, norm=True):
    val = 1 / (sigma * math.sqrt(2*math.pi)) * math.e**(-1/2 * ((x - mu)/sigma)**2)
    if norm:
        z = gauss(mu, sigma, mu, norm=False)
    else:
        z = 1
    return val / z
