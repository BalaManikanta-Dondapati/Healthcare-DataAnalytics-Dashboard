import pandas as pd
from pathlib import Path

# Paths
DATA_PATH = Path("D:/Healthcare-DataAnalytics-Dashboard/data/raw/hospital-inpatient-discharges.csv")


# Load dataset
print("🔹 Loading dataset...")
df = pd.read_csv(DATA_PATH, low_memory=False)

# Basic info
print("\n✅ Dataset Loaded Successfully")
print("Shape (rows, columns):", df.shape)
print("\n📋 Column Names:")
print(df.columns.tolist())

# Data types
print("\n🔍 Data Types:")
print(df.dtypes)

# Missing values
print("\n❌ Missing Value Count (Top 10):")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# Preview data
print("\n👀 Sample Rows:")
print(df.head(5))
