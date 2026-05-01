import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)


# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract 'Year-Month' for grouping
df['Month'] = df['Date'].dt.to_period('M')

# Calculate Total Sales for each row (Quantity * Price)
df['Total_Sales'] = df['Quantity'] * df['Price']

# Group by 'Month' and sum the total sales
monthly_sales = df.groupby('Month')['Total_Sales'].sum()
# Find the month with the highest total sales
best_month =monthly_sales.idxmax()
highest_sales = monthly_sales.max()

print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")


# import pandas as pd

# # Prompt the user for the file name
# file_name = input()

# # Load the data
# df = pd.read_csv(file_name)


# # Find the month with the highest total sales
# best_month =
# highest_sales = 

# print(f"Best month: {best_month}")
# print(f"Total sales: ${highest_sales:.2f}")
