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
                
                # Display financial statements in table format
                st.subheader("Financial Statements")

                # Extracting and displaying financial statements
                try:
                    income_statement_quarterly = pd.read_excel('all_stocks_data.xlsx', sheet_name='Income Statement (Quarterly)')
                    income_statement_annual = pd.read_excel('all_stocks_data.xlsx', sheet_name='Income Statement (Annual)')
                    balance_sheet_quarterly = pd.read_excel('all_stocks_data.xlsx', sheet_name='Balance Sheet (Quarterly)')
                    balance_sheet_annual = pd.read_excel('all_stocks_data.xlsx', sheet_name='Balance Sheet (Annual)')
                    cash_flow_annual = pd.read_excel('all_stocks_data.xlsx', sheet_name='Cash Flow (Annual)')
                    
                    st.write("**Income Statement (Quarterly)**")
                    st.dataframe(income_statement_quarterly[income_statement_quarterly['symbol'].str.upper() == symbol.upper()])

                    st.write("**Income Statement (Annual)**")
                    st.dataframe(income_statement_annual[income_statement_annual['symbol'].str.upper() == symbol.upper()])

                    st.write("**Balance Sheet (Quarterly)**")
                    st.dataframe(balance_sheet_quarterly[balance_sheet_quarterly['symbol'].str.upper() == symbol.upper()])

                    st.write("**Balance Sheet (Annual)**")
                    st.dataframe(balance_sheet_annual[balance_sheet_annual['symbol'].str.upper() == symbol.upper()])

                    st.write("**Cash Flow (Annual)**")
                    st.dataframe(cash_flow_annual[cash_flow_annual['symbol'].str.upper() == symbol.upper()])
                    
                except Exception as e:
                    st.write(f"Error loading financial statements: {e}")
        else:
            st.write(f"No data found for symbol: {symbol.upper()}")

if __name__ == "__main__":
    main()
