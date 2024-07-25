import pandas as pd
from camel.agents import CAMELAgent

class PreprocessAgent(CAMELAgent):
    def process(self, df: pd.DataFrame, langchain) -> pd.DataFrame:
        query = "Preprocess the following dataframe"
        context = {'dataframe': df.to_dict()}
        processed_data = langchain.run(query=query, context=context)
        processed_df = pd.DataFrame.from_dict(processed_data)
        return processed_df


