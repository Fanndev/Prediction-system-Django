import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_dataframe(df: pd.DataFrame):
    df = df.dropna()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    return df