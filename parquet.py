import pandas as pd 
import numpy as np 

#create a fake database
def create_df(size):
    df = pd.DataFrame()
    df['size'] = np.random.choice(['big','medium','small'], size)
    df['age'] = np.random.randint(1, 50, size)
    df['color'] = np.random.choice(['red','blue','yellow','green'], size)
    df['winner'] = np.random.choice(['yes','no'], size)
    date = pd.date_range('2020-01-01','2024-01-01')
    df['date'] = np.random.choice(date, size)
    df['score'] = np.random.uniform(0,10, size)
    return df

def define_type(df):
    df['size'] = df['size'].astype('category')
    df['color'] = df['color'].astype('category')
    df['age'] = df['age'].astype('int16')
    df['winner'] = df['winner'].map({'yes':True,'no':False})
    df['score'] = df['score'].astype('float32')
    return df

df = create_df(1000000)
df.info()
df.to_csv(r"c:\temp\teste.csv")
df.to_parquet(r"c:\temp\teste.parquet")
pd.read_parquet(r"c:\temp\teste.parquet")
