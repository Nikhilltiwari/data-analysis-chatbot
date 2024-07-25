import plotly.express as px
import pandas as pd

def create_plot(query: str, df: pd.DataFrame) -> str:
    if "sales trend" in query and "Q1" in query:
        fig = px.line(df, x='date', y='sales', title='Sales Trend for Q1')
        plot_url = fig.to_html(full_html=False)
        return plot_url
    return "Query not understood"
