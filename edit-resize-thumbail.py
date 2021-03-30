#!/usr/bin/env python3
import glob, os
from PIL import Image

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    rotate = 90
    im_rotated = im.rotate(angle=rotate)
    im_resized = im_rotated.resize((128, 128))
    im_resized.save(file + ".jpg", "JPEG")
    