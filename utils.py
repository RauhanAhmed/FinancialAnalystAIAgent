import plotly.graph_objects as go
import yfinance as yf
import pandas as pd
import yaml
import os

# Function to retrieve a list of stock tickers from a YAML configuration file
def getStockTickers() -> list:
    with open(os.path.join(os.getcwd(), "params.yaml"), "rb") as params:
        params = yaml.safe_load(params)  # Load configuration parameters from YAML file
    return pd.read_csv(params.get("tickerListUrl"))["ticker"].tolist()  # Read tickers from CSV file and return as a list

# Function to fetch historical stock data and generate a candlestick chart
def getCandlestickChartData(ticker: str) -> tuple:
    df = yf.download(ticker, multi_level_index=False)  # Download stock data using Yahoo Finance API
    
    # Create a candlestick chart using Plotly
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    )])

    # Increase overall figure size for better visibility of candlestick width
    fig.update_layout(width=1000, height=600)

    # Remove gaps for non-trading days (e.g., weekends)
    fig.update_xaxes(
        type='date',
        rangebreaks=[dict(bounds=["sat", "mon"])]  # Hides weekends from the chart
    )
    
    # Remove the default range slider below the chart for a cleaner view
    fig.update_layout(xaxis_rangeslider_visible=False)

    return (df.sort_index(ascending=False), fig)  # Return sorted data (most recent first) and the chart
