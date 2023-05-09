import torch
from transformers import Seq2SeqTrainer, Seq2SeqTrainingArguments
from transformers import VisionEncoderDecoderModel
from torch.utils.data import Dataset
from PIL import Image
import pandas as pd
from transformers import TrOCRProcessor
import os 

processor = TrOCRProcessor.from_pretrained(r"./df/checkpoint-10000")
modelname=r"./tuned-trocr-b4-g2-small-10000zithoutx-20epochs"
model = VisionEncoderDecoderModel.from_pretrained(modelname)
# load an image and preprocess it
image = Image.open(r"..\data\images\Fuente3parte_amistoso_7_18.jpg")

ann_df = pd.read_excel(r"../example.xlsx")
for i, row in ann_df.iterrows():
    x, y, h, w = row['x'], row['y'], row['h'], row['w']
    crop_left = max(x, 0)
    crop_upper = max(y, 0)
    crop_right = min(x+w, image.size[0])
    crop_lower = min(y+h, image.size[1])
    crop = image.crop((crop_left, crop_upper, crop_right, crop_lower))
    if crop.size[0] == 0 or crop.size[1] == 0:
        continue
    crop=crop.convert("RGB")
    pixel_values = processor(crop, return_tensors="pt").pixel_values
    # generate the predicted text
    output = model.generate(pixel_values)
    # decode the output into a list of strings
    predicted_text = processor.batch_decode(output, skip_special_tokens=True)
    ann_df.iloc[i,-1]=predicted_text 
ann_df.to_excel(r"../examplecsvwithpred.csv", index=False)
