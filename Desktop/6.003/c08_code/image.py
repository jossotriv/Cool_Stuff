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

    def get_pixel(self, x, y):
        """
        Returns the value of the pixel at location (x, y).
        Raises an exception if the given location is out of range.
        """
        return self.pixels[x + self.width*y]

    def set_pixel(self, x, y, c):
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


    @classmethod
    def from_array(cls, array, normalize=True):
        """
        Convert a 2-d array to an image.
        Input should be specified as a list of lists.  Each internal list
        represents a column in the image, with the top element in the column
        coming first.

        If normalize is True, normalize the image so that the max and min
        elements in the output image are 0 and 255.
        """
        assert bool(array), "array must be nonempty"
        out = Image.new(len(array), len(array[0]))
        realarray = []
        for x in range(len(array)):
            newcol = []
            for y in range(len(array[x])):
                oval = array[x][y]
                assert oval.imag <= 1e-9, "values in newarray must be real"
                newcol.append(oval.real)
            realarray.append(newcol[::-1]) # PIL origin is upper-left
        array = realarray
        allpx = sum((i for i in array), [])
        maxval = max(allpx)
        minval = min(allpx)
        delta = maxval - minval
        for x in range(len(array)):
            for y in range(len(array[x])):
                if normalize:
                    out[x, y] = round((array[x][y] - minval) * (255 / delta))
                else:
                    out[x, y] = round(array[x][y])
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
            return cls(w, h, pixels)

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
        if isinstance(fname, str):
            out.save(fname)
        else:
            out.save(fname, mode)
        out.close()
