import pandas as pd
from camel_agents import CamelAgent

class AnalyzeAgent(CamelAgent):
    def process_query(self, query: str, df: pd.DataFrame) -> str:
        if 'average' in query and 'Q1' in query:
            result = df['sales'].mean()
            return f'The average sales in Q1 is {result}'
        return 'Query not understood'
