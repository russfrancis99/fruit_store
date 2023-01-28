#! /usr/bin/env python3

from PIL import Image
import sys, os

size = (600, 400)
descriptions = 'supplier-data/descriptions'
images = 'supplier-data/images'
for infile in os.listdir(images):
    outfile = images + "/" + os.path.splitext(infile)[0] + ".jpeg"
    if infile != outfile:
        print("")
        print("processing image: ",infile)
        try:
            with Image.open(images + "/" + infile) as im:
                im2 = im.convert('RGB')
                im2.thumbnail(size)
                im2.save(outfile,"JPEG")
                # print("outfile path: ", outfile)
                im.close
        except OSError:
            print("problem saving: ", infile)
