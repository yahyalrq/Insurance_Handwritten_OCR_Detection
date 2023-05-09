import os
import shutil

IMG_DIR = '../data/images'
# annotation directory path
ANN_DIR = '../data/annotations'
# The cropped images will be stored here
CROP_DIR = '../data/crops'


# list all files in the image directory
files = os.listdir(IMG_DIR)

for f in files:
    if f.endswith('.csv'):
        # move CSV file to annotations directory
        shutil.move(os.path.join(IMG_DIR, f), os.path.join(ANN_DIR, f))
    if f.endswith(".xlsx"):
        print("OOOO")
        shutil.move(os.path.join(IMG_DIR, f), os.path.join(ANN_DIR, f))