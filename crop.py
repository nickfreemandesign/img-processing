from PIL import Image
import os, sys

# Get items in directory at relative path
path = "crop-folder/"
dirs = os.listdir( path )

def crop():
    # iterate items in directory
    for item in dirs:
        # if item exists
        if os.path.isfile(path+item):
            # open item as Image
            im = Image.open(path+item)
            # get file name and extension
            f, e = os.path.splitext(path+item)
            # crop image based on size
            imCrop = im.crop((0,0,400,289))
            # save in same directory with new name
            imCrop.save(f + '-cropped.png', 'PNG', quality=90)

crop()
