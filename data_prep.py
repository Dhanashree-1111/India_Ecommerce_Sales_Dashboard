import pandas as pd

try:
    orders = pd.read_csv('Orders.csv')
    details = pd.read_csv('Details.csv')
    
    # 1. Clean column names (removes hidden spaces)
    orders.columns = orders.columns.str.strip()
    details.columns = details.columns.str.strip()

    # 2. Join tables
    df = pd.merge(details, orders, on='Order ID', how='left')

    # 3. Handle the 'Cost' issue
    # If 'Cost' exists, we use it. If not, we calculate it if Profit and Amount exist.
    if 'Cost' in df.columns:
        df['Profit'] = df['Amount'] - df['Cost']
    elif 'Profit' in df.columns and 'Amount' in df.columns:
        # If we have Amount and Profit, we can create the Cost column for the records
        df['Cost'] = df['Amount'] - df['Profit']
    else:
        # If no Cost or Profit exists, we create a dummy Profit for now to keep you moving
        df['Profit'] = df['Amount'] * 0.15 
        print("Note: 'Cost' column not found, calculating estimated 15% profit.")

    # 4. Final Calculations
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
    df['Profit_Margin'] = (df['Profit'] / df['Amount']).round(4)
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month_name()

    # 5. Export
    df.to_csv('Cleaned_Ecommerce_Data.csv', index=False)
    print("Success: 'Cleaned_Ecommerce_Data.csv' created despite the column naming issue!")

except Exception as e:
    print(f"An error occurred: {e}")