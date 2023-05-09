


import pandas as pd

def sample_dataframe():
    # Check if the input DataFrame is empty
    df = pd.read_csv('output.csv')
    df1=df.copy()
    dfx=df1[(df1['text']=='X')|(df1['text']=='x')]
    dfx=dfx.sample(n=5000)
    df1=df1[df1['text']!='X']
    df1=df1[df1['text']!='x']
    df1=pd.concat([df1,dfx])
    # Otherwise, randomly sample 5000 rows from the DataFrame
    df1.to_csv('df.csv')
    print(len(df1))
sample_dataframe()
