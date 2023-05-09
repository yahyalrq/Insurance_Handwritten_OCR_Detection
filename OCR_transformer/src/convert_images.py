import os, sys
from PIL import Image
import cv2
import pandas as pd

# image directory path
IMG_DIR = '../data/images'
# annotation directory path
ANN_DIR = '../data/annotations'
# The cropped images will be stored here
CROP_DIR = '../data/crops'

# list all subfolders in the image directory
folders = os.listdir(IMG_DIR)

for folder_name in folders:
    img_folder = IMG_DIR+"/"+ folder_name
    ann_folder = ANN_DIR+"/" +folder_name
    for f in os.listdir(img_folder):
        os.rename(img_folder+"/"+f,img_folder+os.path.basename(f))
