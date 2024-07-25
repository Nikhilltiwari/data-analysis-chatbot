import pandas as pd
from camel_agents import CamelAgent

class PreprocessAgent(CamelAgent):
    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.dropna()
        df['date'] = pd.to_datetime(df['date'])
        return df
