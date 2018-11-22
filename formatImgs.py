from PIL import Image
import os
import sys

path = sys.argv[1] + "/original/"
full = sys.argv[1] + "/full/"
thumb = sys.argv[1] + "/thumbs/"
dirs = os.listdir(path)

def formatImg():
    for item in dirs:
         if os.path.isfile(path+item):
            # get file paths
            file_name = item.split('.')[0]
            full_path = full + file_name
            thumb_path = thumb + file_name
            # store file as PIL image
            im = Image.open(path+item)
            im2 = Image.open(path+item)
            # convert image to be saved into different format
            rgb_im_full = im.convert('RGB')
            rgb_im_thumb = im2.convert('RGB')
            # resize thumb to different ratio
            rgb_im_thumb = rgb_im_thumb.resize((600, 927), Image.ANTIALIAS)
            # save both images in relative path, with varying qualities
            rgb_im_full.save(full_path + '.jpg', 'JPEG', quality=95, optimize=True, progressive=True)
            rgb_im_thumb.save(thumb_path + '.jpg', 'JPEG', quality=50, optimize=True, progressive=True)
       

formatImg()
