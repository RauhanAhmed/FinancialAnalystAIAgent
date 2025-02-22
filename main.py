# Import necessary modules
from utils import getCandlestickChartData, getStockTickers
from financeAnalystAgent import FinancialAnalystAgent
from dotenv import load_dotenv
import streamlit as st

# Load environment variables 
load_dotenv()

# Initialize the AI-powered financial analyst agent
agent = FinancialAnalystAgent()

# --- Frontend Streamlit App ---
def main():
    # Set up the Streamlit page configuration
    st.set_page_config(page_title="Stock Analysis Dashboard", layout="wide")

    # --- Sidebar ---
    st.sidebar.header("Stock Selector")  # Sidebar section title

    # Fetch the list of available stock tickers
    stockTickers = getStockTickers()

    # Create a dropdown menu to select a stock ticker
    selectedTicker = st.sidebar.selectbox("Select a Stock Ticker", stockTickers)

    # --- Main Screen ---
    st.title("Stock Analysis Dashboard")  # Main dashboard title

    # Display the currently selected stock
    st.subheader(f"Selected Stock: {selectedTicker}")

    # Fetch historical stock data and candlestick chart
    historicalData, candlestickChart = getCandlestickChartData(selectedTicker)

    # Display the historical stock data in a table
    st.markdown("### Historical Data")
    st.dataframe(historicalData, height=300, use_container_width=True)

    # Generate and display the candlestick chart for the selected stock
    st.markdown("### Candlestick Chart")
    st.plotly_chart(candlestickChart, use_container_width=True)

    # --- AI Agent Query Section ---
    st.markdown("### Ask the AI Agent")  # Section for AI-powered insights
    
    # Text area for user to input a query related to stocks
    userQuery = st.text_area("Enter your question related to stocks", height=150)

    # Button to submit the query for AI analysis
    if st.button("Submit Query"):
        with st.spinner("Analyzing your query..."):
            # Process the query using the AI agent and get the response
            response = agent.chatbot(userQuery=userQuery)
        
        # Display the AI agent's response
        st.markdown("#### AI Agent Response:")
        st.write(response)

# Entry point to run the Streamlit app
if __name__ == "__main__":
    main()