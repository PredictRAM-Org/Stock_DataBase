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
    st.sidebar.header("Search Options")

    # Input for stock symbol
    symbol = st.sidebar.text_input("Enter Stock Symbol:")

    # Option to toggle between list view and column view
    view_option = st.sidebar.selectbox(
        "Select View Option",
        ["Column View", "List View"]
    )

    # Filter data based on the input symbol
    if symbol:
        result = data[data['symbol'].str.upper() == symbol.upper()]

        if not result.empty:
            st.write(f"Results for symbol: {symbol.upper()}")
            
            if view_option == "Column View":
                # Display data in column view
                st.subheader("Column View")
                st.dataframe(result)
            elif view_option == "List View":
                # Display all data as an interactive list view
                st.subheader("List View")
                
                # Convert result to a dictionary for a list view
                result_dict = result.to_dict(orient='records')[0]
                
                # Display each key-value pair as a list item
                for key, value in result_dict.items():
                    st.write(f"**{key}:** {value}")
        else:
            st.write(f"No data found for symbol: {symbol.upper()}")

if __name__ == "__main__":
    main()
