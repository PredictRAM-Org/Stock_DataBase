import pandas as pd

def load_financial_statements():
    excel_file = 'all_stocks_data.xlsx'

    # Load the Excel file and get the sheet names
    xl = pd.ExcelFile(excel_file)
    print("Available sheet names:", xl.sheet_names)

    # Update the sheet names based on the actual names in the file
    income_statement_quarterly = pd.read_excel(excel_file, sheet_name='Income Statement (Quarterly)')
    income_statement_annual = pd.read_excel(excel_file, sheet_name='Income Statement (Annual)')
    balance_sheet_quarterly = pd.read_excel(excel_file, sheet_name='Balance Sheet (Quarterly)')
    balance_sheet_annual = pd.read_excel(excel_file, sheet_name='Balance Sheet (Annual)')
    cash_flow_annual = pd.read_excel(excel_file, sheet_name='Cash Flow (Annual)')

    return income_statement_quarterly, income_statement_annual, balance_sheet_quarterly, balance_sheet_annual, cash_flow_annual

def main():
    income_statement_quarterly, income_statement_annual, balance_sheet_quarterly, balance_sheet_annual, cash_flow_annual = load_financial_statements()
    # Further processing

if __name__ == "__main__":
    main()
