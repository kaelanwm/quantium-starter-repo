import pandas as pd
from pathlib import Path

# Path to the data folder
Data = Path("data")

# Load all three CSVs
files = [ 
    Data / "daily_sales_data_0.csv",
    Data / "daily_sales_data_1.csv",
    Data / "daily_sales_data_2.csv"
]

df_list =[]

for f in files:
    df = pd.read_csv(f)

    # Filter for Pink Morsel only
    df = df[df["product"] == "pink morsel"]

    # Clean price column by removing $ and converting to float
    df["price"] = df["price"].replace('[\\$,]', '', regex=True).astype(float)

    # Compute Sales = quanitity * price
    df["sales"] = df["quantity"] * df["price"]

    # Keep only the needed columns
    df = df[["sales", "date", "region"]]

    df_list.append(df)

# Combine all three into one dataframe
final_df = pd.concat(df_list, ignore_index=True)

# Save the output file
output_path = Data / "pink_morsel_sales.csv"
final_df.to_csv(output_path, index=False)

print(f"Pink Morsel sales data saved to {output_path}")
