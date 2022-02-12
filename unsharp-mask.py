#!/usr/bin/env python3
#new file created
import os, glob
from PIL import Image, ImageFilter

from multiprocessing import Process
path = os.getcwd()
os.chdir(path)
def unsharp_mask():
    for infile in glob.glob("*.jpg"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im1 = im.filter(ImageFilter.UnsharpMask(radius=2, percent=100, threshold=10))
        im1.save(file + ext, quality=100)
        im1.show()
        return im1
        


if __name__ == '__main__':
    p = Process(target=unsharp_mask)
    p.start()
    p.join()