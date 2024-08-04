import streamlit as st
import pandas as pd
import ast
from sklearn.preprocessing import MinMaxScaler  # Make sure scikit-learn is installed

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

                st.subheader("Detailed Data")
                st.write("### Additional Metrics")
                detailed_data1 = result[['exDividendDate', 'payoutRatio', 'fiveYearAvgDividendYield', 'beta', 'volume', 'regularMarketVolume', 
                                         'averageVolume', 'averageVolume10days', 'averageDailyVolume10Day', 'bid', 'ask', 'marketCap', 
                                         'fiftyTwoWeekLow', 'fiftyTwoWeekHigh', 'priceToSalesTrailing12Months', 'fiftyDayAverage', 
                                         'twoHundredDayAverage', 'trailingAnnualDividendRate', 'trailingAnnualDividendYield', 'currency', 
                                         'enterpriseValue', 'profitMargins', 'floatShares', 'sharesOutstanding', 'heldPercentInsiders', 
                                         'heldPercentInstitutions', 'impliedSharesOutstanding', 'bookValue', 'priceToBook', 
                                         'lastFiscalYearEnd', 'nextFiscalYearEnd', 'mostRecentQuarter', 'netIncomeToCommon', 
                                         'trailingEps', 'lastSplitFactor', 'lastSplitDate', 'enterpriseToRevenue', 'enterpriseToEbitda', 
                                         '52WeekChange', 'lastDividendValue', 'lastDividendDate']].T
                st.table(detailed_data1)

                st.write("### Recommendation and Financial Ratios")
                detailed_data2 = result[['recommendationKey', 'totalCash', 'totalCashPerShare', 'ebitda', 'totalDebt', 'quickRatio', 
                                         'currentRatio', 'totalRevenue', 'debtToEquity', 'revenuePerShare', 'returnOnAssets', 
                                         'returnOnEquity', 'freeCashflow', 'operatingCashflow', 'revenueGrowth', 'grossMargins', 
                                         'ebitdaMargins', 'operatingMargins', 'financialCurrency', 'trailingPegRatio', 'forwardPE', 
                                         'trailingPE']].T
                st.table(detailed_data2)

                st.write("### Industry Comparison Ratios")
                
                # Prepare data for table and chart
                stock_metrics = result[['forwardPE', 'trailingPE', 'debtToEquity', 'currentRatio', 'quickRatio', 
                                        'ebitda', 'totalDebt', 'returnOnAssets', 'returnOnEquity', 'revenueGrowth', 
                                        'grossMargins', 'ebitdaMargins', 'operatingMargins']].T
                stock_metrics.columns = ['Stock Value']

                industry_metrics = result[['industry_forwardPE', 'industry_trailingPE', 'industry_debtToEquity', 
                                           'industry_currentRatio', 'industry_quickRatio', 'industry_ebitda', 
                                           'industry_totalDebt', 'industry_returnOnAssets', 'industry_returnOnEquity', 
                                           'industry_revenueGrowth', 'industry_grossMargins', 'industry_ebitdaMargins', 
                                           'industry_operatingMargins']].T
                industry_metrics.columns = ['Industry Value']

                # Normalize the data
                scaler = MinMaxScaler()
                stock_normalized = pd.DataFrame(scaler.fit_transform(stock_metrics[['Stock Value']]), 
                                                columns=['Stock Value (Normalized)'], 
                                                index=stock_metrics.index)
                industry_normalized = pd.DataFrame(scaler.fit_transform(industry_metrics[['Industry Value']]), 
                                                   columns=['Industry Value (Normalized)'], 
                                                   index=industry_metrics.index)

                # Combine normalized data for comparison
                comparison_df = pd.concat([stock_normalized, industry_normalized], axis=1)
                st.table(comparison_df)

                # Plot normalized data
                st.bar_chart(comparison_df)

                st.write("### Company Officers")
                # Expand companyOfficers data to DataFrame
                if isinstance(result['companyOfficers'].values[0], str):
                    officers_list = ast.literal_eval(result['companyOfficers'].values[0])
                else:
                    officers_list = result['companyOfficers'].values[0]
                
                officers_df = pd.DataFrame(officers_list)
                st.table(officers_df)

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
