import pandas as pd
import os

path = 'C:/Users/bmazari.ieu2020/Desktop/OCRSL/data/annotations/crops'
data = []

for filename in os.listdir(path):
    if filename.endswith('.csv'):
        filepath = os.path.join(path, filename)
        df = pd.read_csv(filepath)
        label = df['text'].values[0]
        filename= filename[:-4]
        filename=filename+'.jpg'
        data.append([filename, label])

df_new = pd.DataFrame(data, columns=['file_name', 'text'])
df_new.to_csv('output.csv', index=False)