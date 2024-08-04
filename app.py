import streamlit as st
import pandas as pd

# Load data
@st.cache
def load_data():
    return pd.read_excel('all_stocks_data.xlsx')

data = load_data()

# Streamlit app layout
st.title("Stock Analysis Dashboard")

# Sidebar for stock selection
st.sidebar.header("Select Stock")
stock_options = data['symbol'].unique()
selected_stock = st.sidebar.selectbox("Choose a stock", stock_options)

# Filter data for the selected stock
selected_stock_data = data[data['symbol'] == selected_stock].iloc[0]

# Display selected stock information
st.subheader(f"Stock Details for {selected_stock}")
st.write(f"**Name:** {selected_stock_data['longName']}")
st.write(f"**Industry:** {selected_stock_data['industry']}")
st.write(f"**Sector:** {selected_stock_data['sector']}")
st.write(f"**Current Price:** ${selected_stock_data['currentPrice']}")
st.write(f"**Market Cap:** ${selected_stock_data['marketCap']}")

# Create an interactive dashboard
st.subheader("Stock Metrics")
metrics = [
    'trailingPegRatio', 'forwardPE', 'trailingPE', 'ebitda', 'totalDebt',
    'quickRatio', 'currentRatio', 'totalRevenue', 'debtToEquity',
    'revenuePerShare', 'returnOnAssets', 'returnOnEquity', 'freeCashflow',
    'operatingCashflow', 'revenueGrowth', 'grossMargins', 'ebitdaMargins',
    'operatingMargins'
]

selected_metrics = st.multiselect("Select metrics to display", metrics, default=metrics)
st.write(selected_stock_data[selected_metrics])

# Comparison between stock and industry metrics
st.subheader("Comparison with Industry Metrics")
industry_metrics = [
    'industry_forwardPE', 'industry_trailingPE', 'industry_debtToEquity',
    'industry_currentRatio', 'industry_quickRatio', 'industry_ebitda',
    'industry_totalDebt', 'industry_returnOnAssets', 'industry_returnOnEquity',
    'industry_revenueGrowth', 'industry_grossMargins', 'industry_ebitdaMargins',
    'industry_operatingMargins'
]

industry_data = data[data['industry'] == selected_stock_data['industry']].mean()

def display_comparison(stock_value, industry_value, metric_name):
    st.write(f"**{metric_name}:**")
    st.write(f"Stock: {stock_value}")
    st.write(f"Industry Average: {industry_value}")
    if pd.notna(stock_value) and pd.notna(industry_value):
        if stock_value > industry_value:
            st.write("**The stock is performing better than the industry average.**")
        else:
            st.write("**The stock is performing worse than the industry average.**")

for metric in metrics:
    if metric in selected_stock_data.index and metric in industry_data.index:
        display_comparison(
            selected_stock_data[metric],
            industry_data[metric.replace('totalDebt', 'industry_totalDebt')], # Adjust if needed
            metric
        )

# Run Streamlit app
if __name__ == "__main__":
    st.run()
