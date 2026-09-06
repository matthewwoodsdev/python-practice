# Selecting data in pandas
# Matthew Woods - practice file

import pandas as pd

sales = {"user_id": ["KM37", "PR19", "YU88", "NT43", "IW06"],
         "order_value": [197.75, 208.21, 134.99, 153.54, 379.47]}

sales_df = pd.DataFrame(sales)

# Selecting one column returns a Series
print(sales_df["order_value"])

# Double brackets return a DataFrame
print(sales_df[["order_value"]])

# Selecting several columns
print(sales_df[["user_id", "order_value"]])

# Filtering rows with a condition
print(sales_df[sales_df["order_value"] > 200])

# Sorting by a column
print(sales_df.sort_values("order_value"))

# Sorting highest first
print(sales_df.sort_values("order_value", ascending=False))
