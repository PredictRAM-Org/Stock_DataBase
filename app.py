import streamlit as st
import pandas as pd

# Load data from the Excel file
@st.cache_data
def load_data():
    return pd.read_excel('all_stocks_data.xlsx')

def main():
    st.title("Stock Data Search")

    # Load data
    data = load_data()

    # Display available columns for debugging
    st.write("Available columns in the dataset:")
    st.write(data.columns.tolist())

    # Sidebar for user input
    st.sidebar.header("Search Options")

    # Input for stock symbol
    symbol = st.sidebar.text_input("Enter Stock Symbol:")

    # Filter data based on the input symbol
    if symbol:
        result = data[data['symbol'].str.upper() == symbol.upper()]

        if not result.empty:
            st.write(f"Results for symbol: {symbol.upper()}")
            
            # Display columns with proper labels
            display_columns = ['symbol', 'shortName', 'longName', 'industry', 'sector', 'currentPrice',
                               'previousClose', 'dayLow', 'dayHigh', 'marketCap', 'volume', 'beta',
                               'priceToBook', 'trailingEps', 'enterpriseValue', 'totalCash', 'totalDebt',
                               'returnOnAssets', 'returnOnEquity']

            # Ensure all columns exist before trying to display them
            valid_columns = [col for col in display_columns if col in data.columns]
            st.subheader("Stock Details")
            st.write(result[valid_columns])
        else:
            st.write(f"No data found for symbol: {symbol.upper()}")

if __name__ == "__main__":
    main()
