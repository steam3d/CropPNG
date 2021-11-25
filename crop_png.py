from PIL import Image
import numpy as np
from os import listdir

# https://stackoverflow.com/questions/1905421/crop-a-png-image-to-its-minimum-size
def crop(png_image_name):
    im = Image.open(png_image_name)
    print(im.size)
    im.getbbox()
    im2 = im.crop(im.getbbox())
    print(im2.size)
    im2.save("_" + png_image_name)

for f in listdir('.'):
    if f.endswith('.png'):
        crop(f)
