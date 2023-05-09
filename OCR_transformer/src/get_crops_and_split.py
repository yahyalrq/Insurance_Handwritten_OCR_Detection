import os
import sys
import pandas as pd
from PIL import Image
from sklearn.model_selection import train_test_split

ANNOTATION_DIR = '../data/annotations'
IMG_DIR = "../data/images"
CROP_DIR = "../data/crops"
ANNOTATION_DIR_CROPS = '../data/annotations/crops'

# Create train-test split
img_names = []
for ann_file in os.listdir(ANNOTATION_DIR):
    if ann_file.endswith('.csv'):
        img_names.append(os.path.splitext(ann_file)[0] + '.jpg')

print('passed')
# Process train images

for img_name in img_names:
    ann_file = os.path.splitext(img_name)[0] + '.csv'
    ann_path = os.path.join(ANNOTATION_DIR, ann_file)
    ann_df = pd.read_csv(ann_path)

    img_path = os.path.join(IMG_DIR, img_name)
    img = Image.open(img_path)

    for i, row in ann_df.iterrows():
        x, y, h, w, text = row['x'], row['y'], row['h'], row['w'],row['text']
        crop = img.crop((x, y, x+w, y+h))
        if pd.isnull(text) or text=="":
            continue
        if crop.size[0] == 0 or crop.size[1] == 0:
            continue
        crop_path = os.path.join(CROP_DIR, f"{img_name}_{i}.jpg")
        crop.save(crop_path)

        ann_row = pd.DataFrame({'x': x, 'y': y, 'h': h, 'w': w, 'text':text}, index=[0])
        ann_filename = os.path.splitext(os.path.basename(crop_path))[0] + '.csv'
        ann_path = os.path.join(ANNOTATION_DIR_CROPS, ann_filename)
        ann_row.to_csv(ann_path, index=False)


    


"""
def ocr(img):
    img = img_to_array(img)
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)[0]
    if pred > 0.5:
        return pytesseract.image_to_string(img, config=custom_config)
    else:
        return None
"""