import pandas as pd

# Raw data load
df = pd.read_csv("Raw_Data/Sales_raw.xlsx.csv")

print("Original Data:")
print(df.head())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove completely empty rows
df = df.dropna(how="all")

# Remove spaces from column names
df.columns = df.columns.str.strip()

# Remove extra spaces from text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype(str).str.strip()

# Save cleaned data
df.to_csv("Cleaned_Data/sales_cleaned.csv", index=False)

print("\nCleaning completed successfully!")
print("Cleaned rows:", len(df))
print("Cleaned file saved in Cleaned_Data folder.")