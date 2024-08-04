import streamlit as st
import pandas as pd

# Load data from the Excel file
@st.cache_data
def load_data():
    return pd.read_excel('all_stocks_data.xlsx')

def main():
    st.title("Comprehensive Stock Dashboard")

    # Load data
    data = load_data()

    # Sidebar for search and view options
    st.sidebar.header("Search Options")
    
    # Input for stock symbol
    symbol = st.sidebar.text_input("Enter Stock Symbol:")
    
    # Option to toggle between different views
    view_option = st.sidebar.selectbox(
        "Select View Option",
        ["Dashboard View", "List View"]
    )

    # Filter data based on the input symbol
    if symbol:
        result = data[data['symbol'].str.upper() == symbol.upper()]

        if not result.empty:
            st.write(f"Results for symbol: {symbol.upper()}")
            
            if view_option == "Dashboard View":
                st.subheader("Company Overview")
                st.write(f"**Symbol:** {result['symbol'].values[0]}")
                st.write(f"**Name:** {result['shortName'].values[0]}")
                st.write(f"**Address:** {result['address1'].values[0]}, {result['address2'].values[0]}, {result['city'].values[0]}, {result['zip'].values[0]}, {result['country'].values[0]}")
                st.write(f"**Website:** {result['website'].values[0]}")
                st.write(f"**Industry:** {result['industry'].values[0]}")
                st.write(f"**Sector:** {result['sector'].values[0]}")
                st.write(f"**Business Summary:** {result['longBusinessSummary'].values[0]}")

                st.subheader("Stock Information")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.write(f"**Current Price:** {result['currentPrice'].values[0]}")
                    st.write(f"**Previous Close:** {result['previousClose'].values[0]}")
                    st.write(f"**Market Cap:** {result['marketCap'].values[0]}")
                    st.write(f"**52 Week High:** {result['fiftyTwoWeekHigh'].values[0]}")
                    st.write(f"**52 Week Low:** {result['fiftyTwoWeekLow'].values[0]}")

                with col2:
                    st.write(f"**Beta:** {result['beta'].values[0]}")
                    st.write(f"**Dividend Yield:** {result['trailingAnnualDividendYield'].values[0]}")
                    st.write(f"**Price-to-Sales Ratio:** {result['priceToSalesTrailing12Months'].values[0]}")
                    st.write(f"**P/E Ratio:** {result['forwardPE'].values[0]}")
                    st.write(f"**Volume:** {result['volume'].values[0]}")

                with col3:
                    st.write(f"**Price-to-Book Ratio:** {result['priceToBook'].values[0]}")
                    st.write(f"**Profit Margins:** {result['profitMargins'].values[0]}")
                    st.write(f"**Debt-to-Equity Ratio:** {result['debtToEquity'].values[0]}")
                    st.write(f"**Return on Assets:** {result['returnOnAssets'].values[0]}")
                    st.write(f"**Return on Equity:** {result['returnOnEquity'].values[0]}")

                st.subheader("Industry Parameters")
                industry_params = result[['industry_forwardPE', 'industry_trailingPE', 'industry_debtToEquity', 'industry_returnOnAssets', 'industry_returnOnEquity']].T
                industry_params.columns = ['Value']
                st.table(industry_params)

                st.subheader("Historical Performance")
                historical_data = result[['fiftyDayAverage', 'twoHundredDayAverage', 'volume', 'averageVolume']].T
                st.line_chart(historical_data)

                st.subheader("Financial Metrics")
                metrics_data = result[['profitMargins', 'priceToBook', 'debtToEquity', 'returnOnAssets', 'returnOnEquity']].T
                st.bar_chart(metrics_data)

            elif view_option == "List View":
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
