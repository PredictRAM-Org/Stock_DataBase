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

    # User input for stock symbol
    symbol = st.text_input("Enter Stock Symbol:")

    if symbol:
        # Filter data based on the input symbol
        result = data[data['symbol'].str.upper() == symbol.upper()]

        if not result.empty:
            st.write(f"Results for symbol: {symbol.upper()}")
            st.dataframe(result)
        else:
            st.write(f"No data found for symbol: {symbol.upper()}")

if __name__ == "__main__":
    main()
