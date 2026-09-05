# pandas basics
# Matthew Woods - practice file

# pandas is a package - install it first with:
# python3 -m pip install pandas

# Import with an alias to shorten the code
import pandas as pd

# A dictionary of sales data
sales = {"user_id": ["KM37", "PR19", "YU88"],
         "order_value": [197.75, 208.21, 134.99]}

# Convert the dictionary to a DataFrame
sales_df = pd.DataFrame(sales)
print(sales_df)

# Check the data type
print(type(sales_df))

# head() - preview the first five rows
print(sales_df.head())

# info() - column names, counts and data types
print(sales_df.info())

# Reading a CSV file in the current directory
# sales_df = pd.read_csv("sales.csv")
