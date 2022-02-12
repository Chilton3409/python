#!/usr/bin/env python3
#New file created
import os
from PIL import Image
import glob
"""
I want to loop through all the images in the directory and change them from tiff to jpg
start with basic steps and then incorporate functions. Ideally, all I will have to do is add images to the images 
directory, run the script and have jpgs in one file and raw images in the other. Optionally, I could delete the raw files

"""
#change to images directory and sort the files
os.chdir("images")
path = os.getcwd()
os.listdir(path)
sorted(path)
for infile in glob.glob("*.tif"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im_converted = im.convert('RGB')
    im_converted.save(file + ".jpeg", "JPEG")

"""
if os.path.isdir("raw") == True:
        os.chdir("raw")
else:
    os.mkdir("raw")
    os.chdir("raw")
"""
#create raw and fin-jpegs directory, then in your terminal run mv *.tif to raw
#in the terminal run mv *.jpeg to fin-jpegs. 