import numpy
from numpy.fft import fft, fft2, ifft, ifft2
from PIL import Image, ImageSequence
from math import e, pi
j = 1j


def array_from_image(image):
    im_arr = numpy.fromstring(image.convert('L').tobytes(), dtype=numpy.uint8)
    im_arr = im_arr.reshape((image.size[1], image.size[0]))
    return im_arr.astype(numpy.float64)/255


def png_to_array(fname):
    """
    Load the PNG image with the given filename into a numpy array.
    """
    with Image.open(fname) as image:
        return array_from_image(image)


def image_from_array(arr):
    h = len(arr)
    w = len(arr[0])
    out = Image.new(mode='L', size=(w, h))
    out.putdata(numpy.around(255*arr).reshape(w*h))
    return out


def array_to_png(arr, fname):
    image_from_array(arr).save(fname)


def gif_to_array_list(fname):
    with Image.open(fname) as im:
        return [array_from_image(frame) for frame in ImageSequence.Iterator(im)]


def array_list_to_gif(arr, fname, duration=1, loop=0):
    out = [image_from_array(i) for i in arr]
    out[0].save(fname, save_all=True, append_images=out[1:], duration=duration, loop=loop)


