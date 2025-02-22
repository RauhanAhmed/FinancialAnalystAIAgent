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
    # Download stock data using Yahoo Finance API
    df = yf.download(ticker, multi_level_index=False)

    # Create a candlestick chart using Plotly with custom styling
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        increasing_line_color='limegreen',          
        decreasing_line_color='crimson',              
        increasing_fillcolor='rgba(50,205,50,0.3)',    
        decreasing_fillcolor='rgba(220,20,60,0.3)'     
    )])

    # Update layout for better visualization and aesthetics
    fig.update_layout(
        title=f'Candlestick Chart for {ticker}',
        xaxis_title='Date',
        yaxis_title='Price',
        width=1000,
        height=600,
        xaxis_rangeslider_visible=False  # Remove the range slider for a cleaner view
    )

    # Remove gaps for non-trading days (e.g., weekends)
    fig.update_xaxes(
        type='date',
        rangebreaks=[dict(bounds=["sat", "mon"])]
    )
    
    # Return the data (with most recent dates first) and the styled chart
    return (df.sort_index(ascending=False), fig)