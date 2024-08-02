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
            st.subheader("Stock Details")
            st.write(result[['symbol', 'shortName', 'longName', 'industry', 'sector', 'currentPrice', 
                             'previousClose', 'dayLow', 'dayHigh', 'marketCap', 'volume', 'beta', 
                             'peRatio', 'priceToBook', 'trailingEps', 'earningsDate', 'dividendYield', 
                             'enterpriseValue', 'totalCash', 'totalDebt', 'returnOnAssets', 'returnOnEquity']])
            
            # Additional detailed information
            st.subheader("Detailed Financial Information")
            st.write(result[['longBusinessSummary', 'companyOfficers', 'priceHint', 'payoutRatio', 
                             'fiveYearAvgDividendYield', 'regularMarketPreviousClose', 'regularMarketOpen',
                             'regularMarketDayLow', 'regularMarketDayHigh', 'fiftyTwoWeekLow', 
                             'fiftyTwoWeekHigh', 'priceToSalesTrailing12Months', 'fiftyDayAverage', 
                             'twoHundredDayAverage', 'trailingAnnualDividendRate', 
                             'trailingAnnualDividendYield', 'currency', 'enterpriseValue', 'profitMargins', 
                             'floatShares', 'sharesOutstanding', 'heldPercentInsiders', 
                             'heldPercentInstitutions', 'impliedSharesOutstanding', 'bookValue', 
                             'priceToBook', 'lastFiscalYearEnd', 'nextFiscalYearEnd', 
                             'mostRecentQuarter', 'netIncomeToCommon', 'trailingEps', 
                             'lastSplitFactor', 'lastSplitDate', 'enterpriseToRevenue', 
                             'enterpriseToEbitda', '52WeekChange', 'SandP52WeekChange', 
                             'lastDividendValue', 'lastDividendDate', 'exchange', 'quoteType', 
                             'uuid', 'messageBoardId', 'gmtOffSetMilliseconds', 'recommendationKey', 
                             'totalCash', 'totalCashPerShare', 'ebitda', 'totalDebt', 'quickRatio', 
                             'currentRatio', 'totalRevenue', 'debtToEquity', 'revenuePerShare', 
                             'returnOnAssets', 'returnOnEquity', 'freeCashflow', 'operatingCashflow', 
                             'revenueGrowth', 'grossMargins', 'ebitdaMargins', 'operatingMargins', 
                             'financialCurrency', 'trailingPegRatio', 'forwardPE', 'trailingPE']])
        else:
            st.write(f"No data found for symbol: {symbol.upper()}")

if __name__ == "__main__":
    main()
