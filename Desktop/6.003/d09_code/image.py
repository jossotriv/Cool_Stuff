import math
import numpy
from numpy.fft import fft2, ifft2, fftshift, ifftshift
from PIL import Image as PILImage


class Image:
    """
    A class to represent images, including support for a few different image
    manipulations.
    """
    def __init__(self, width, height, pixels):
        self.width = width
        """The width of the image, in pixels."""
        self.height = height
        """The height of the image, in pixels."""
        self.pixels = pixels
        """The pixel values of the image, in row-major order."""

    def get_pixel(self, y, x):
        """
        Returns the value of the pixel at location (x, y).
        Raises an exception if the given location is out of range.
        """
        return self.pixels[x + self.width*y]

    def normalize_1(self):
        """
        Returns a copy of the image with values normalized to be in the range
        0-1
        """
        out = Image.new(self.width, self.height)
        maxval = max(abs(i) for i in self.pixels)
        for c in range(self.width):
            for r in range(self.height):
                out[r, c] = self[r, c]/maxval
        return out

    def set_pixel(self, y, x, c):
        """
        Sets the value of the pixel at location x
        """
        self.pixels[x + self.width*y] = c

    def copy(self):
        """
        Return a new instance of Image with identical size and pixels to this
        image.
        """
        out = Image.new(self.width, self.height)
        out.pixels = self.pixels[:]
        return out

    def __getitem__(self, ix):
        return self.get_pixel(*ix)

    def __setitem__(self, ix, val):
        return self.set_pixel(*ix, val)

    def fft(self, centered=False):
        """
        Computest the 2-D DFT of this image and returns the result as a numpy
        array with (kx_0, ky=0) in the upper-left corner.

        If centered=True, put (0,0) in the center instead.
        """
        out = fft2(self.to_array())
        if centered:
            out = fftshift(out)
        return out

    @classmethod
    def from_fft(cls, x, centered=False):
        """
        Return an instance of Image containing the spatial data represented by
        the given DFT coefficients.

        If centered=True, assume that (kx=0, ky=0) is in the center of the
        given FFT; otherwise return False.
        """
        if centered:
            x = ifftshift(x)
        return Image.from_array(ifft2(x))

    def save_fft_images(self, basename, intensity_scale=1):
        """
        Saves images of the FFT magnitude and phase, with (Kx=0, Ky=0) in the
        center.
        """
        X = self.fft()
        X_mag = abs(X)
        X_mag[0,0] = 0
        X_mag[0,0] = numpy.max(X_mag)
        X_mag *= intensity_scale
        Image.from_array(fftshift(X_mag)).save('%s_mag.png' % basename)
        Image.from_array(fftshift(numpy.angle(X)), norm_bounds=(-math.pi, math.pi)).save('%s_phase.png' % basename)

    def zoom(self, factor):
        """
        Returns a new Image object representing a scaled version of this image.
        The scaling factor must be an integer >= 1.
        """
        assert isinstance(factor, int), "factor must be an integer."
        assert factor > 0, "factor must be 1 or greater"
        out = Image.new(self.width * factor, self.height * factor)
        for x in range(self.width):
            for y in range(self.height):
                for dx in range(factor):
                    for dy in range(factor):
                        new_x = factor*x + dx
                        new_y = factor*y + dy
                        out[new_x, new_y] = self[x, y]
        return out


    def to_array(self):
        """
        Return the pixels of this image as a numpy array indexed by (row, column)
        """
        return numpy.array([[self[r, c] for c in range(self.width)] for r in range(self.height)])

    @classmethod
    def from_array(cls, array, normalize=True, norm_bounds=None):
        """
        Convert a 2-d array to an image.
        Input should be specified as a list of lists.  Each internal list
        represents a column in the image, with the top element in the column
        coming first.

        If normalize is True, normalize the image so that the max and min
        elements in the output image are 0 and 255.
        """
        assert len(array) != 0 and len(array[0]) != 0, "array must be nonempty"
        realarray = []
        for r in range(len(array)):
            newrow = []
            for c in range(len(array[r])):
                oval = array[r][c]
                assert oval.imag <= 1e-9, "values in newarray must be real: %s" % oval
                newrow.append(oval.real)
            realarray.append(newrow) # PIL origin is upper-left
        array = realarray
        allpx = sum((i for i in array), [])
        if norm_bounds is None:
            maxval = max(allpx)
            minval = min(allpx)
        else:
            minval, maxval = sorted(norm_bounds)
        delta = maxval - minval
        out = Image.new(len(array[0]), len(array))
        for r in range(len(array)):
            for c in range(len(array[r])):
                if normalize:
                    out[r, c] = round((array[r][c] - minval) * (255 / delta))
                else:
                    out[r, c] = round(array[r][c])
        return out

    @classmethod
    def from_file(cls, fname):
        """
        Loads an image from the given file and returns an instance of this
        class representing that image.  This also performs conversion to
        grayscale.

        Invoked as, for example:
           i = Image.load('test_images/cat.png')
        """
        with open(fname, 'rb') as img_handle:
            img = PILImage.open(img_handle)
            img_data = img.getdata()
            if img.mode.startswith('RGB'):
                pixels = [round(.299*p[0] + .587*p[1] + .114*p[2]) for p in img_data]
            elif img.mode == 'LA':
                pixels = [p[0] for p in img_data]
            elif img.mode == 'L':
                pixels = list(img_data)
            else:
                raise ValueError('Unsupported image mode: %r' % img.mode)
            w, h = img.size
            return cls(w, h, pixels).normalize_1()

    @classmethod
    def new(cls, width, height):
        """
        Creates a new blank image (all 0's) of the given height and width.

        Invoked as, for example:
            i = Image.new(640, 480)
        """
        return cls(width, height, [0 for i in range(width*height)])

    def save(self, fname, mode='PNG'):
        """
        Saves the given image to disk or to a file-like object.  If fname is
        given as a string, the file type will be inferred from the given name.
        If fname is given as a file-like object, the file type will be
        determined by the 'mode' parameter.
        """
        out = PILImage.new(mode='L', size=(self.width, self.height))
        out.putdata(self.pixels)
        #out.putdata([int(i*255) for i in self.pixels])
        if isinstance(fname, str):
            out.save(fname)
        else:
            out.save(fname, mode)
        out.close()
