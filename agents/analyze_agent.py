import pandas as pd
from camelagents.camel_agent import CAMELAgent

class AnalyzeAgent(CAMELAgent):
    def process_query(self, query: str, df: pd.DataFrame, langchain) -> str:
        context = {'dataframe': df.to_dict()}
        analysis_result = langchain.run(query=query, context=context)
        return analysis_result




