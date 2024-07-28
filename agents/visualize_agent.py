import pandas as pd
from camelagents.camel_agent import CAMELAgent
import plotly.express as px

class VisualizeAgent(CAMELAgent):
    def create_plot(self, query: str, df: pd.DataFrame, langchain) -> str:
        context = {'dataframe': df.to_dict()}
        visualization_instructions = langchain.run(query=query, context=context)
        
        if "line chart" in visualization_instructions:
            fig = px.line(df, x='date', y='sales', title='Sales Trend for Q1')
            plot_url = fig.to_html(full_html=False)
            return plot_url
        return "Visualization query not understood"





