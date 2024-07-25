import pandas as pd

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'])
    return df
