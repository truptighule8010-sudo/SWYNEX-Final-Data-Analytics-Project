import pandas as pd

# Load cleaned data
df = pd.read_csv("Cleaned_Data/sales_cleaned.csv")

print("===== TITANIC DATA ANALYSIS =====")

# Basic information
print("\nTotal Passengers:", len(df))
print("Total Columns:", len(df.columns))

# Survival analysis
print("\n===== SURVIVAL ANALYSIS =====")
print("Total Survivors:", df["Survived"].sum())
print("Survival Rate:", round(df["Survived"].mean() * 100, 2), "%")

# Survival by gender
print("\n===== SURVIVAL BY GENDER =====")
print(df.groupby("Sex")["Survived"].mean() * 100)

# Survival by passenger class
print("\n===== SURVIVAL BY CLASS =====")
print(df.groupby("Pclass")["Survived"].mean() * 100)

# Passengers by class
print("\n===== PASSENGERS BY CLASS =====")
print(df["Pclass"].value_counts().sort_index())

# Average age
print("\nAverage Age:", round(df["Age"].mean(), 2))

# Average fare
print("Average Fare:", round(df["Fare"].mean(), 2))

# Embarked passengers
print("\n===== PASSENGERS BY EMBARKED PORT =====")
print(df["Embarked"].value_counts())

print("\n===== ANALYSIS COMPLETED =====")
