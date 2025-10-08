import pandas as pd
import numpy as np
import os

# File paths
RAW_DATA_PATH = os.path.join("data", "raw", "hospital-inpatient-discharges.csv")
CLEAN_DATA_PATH = os.path.join("data", "processed", "hospital_cleaned.csv")

print("🔹 Loading raw dataset...")
df = pd.read_csv(RAW_DATA_PATH, low_memory=False)
print("✅ Raw data loaded successfully")

# --- Step 1: Drop unnecessary columns ---
drop_cols = ['index', 'Operating Certificate Number', 'Attending Provider License Number',
             'Operating Provider License Number', 'Other Provider License Number']
df.drop(columns=drop_cols, inplace=True, errors='ignore')

# --- Step 2: Handle missing values ---
# Drop rows missing key information
df.dropna(subset=['Facility Name', 'Total Charges', 'Total Costs'], inplace=True)

# Fill missing text columns with 'Unknown'
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna('Unknown')

# Fill missing numeric columns with median
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

# --- Step 3: Convert numeric columns properly ---
df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce')
df['Total Costs'] = pd.to_numeric(df['Total Costs'], errors='coerce')

# --- Step 4: Remove duplicates ---
df.drop_duplicates(inplace=True)

# --- Step 5: Save cleaned data ---
os.makedirs(os.path.dirname(CLEAN_DATA_PATH), exist_ok=True)
df.to_csv(CLEAN_DATA_PATH, index=False)

print(f"✅ Data cleaning complete! Cleaned file saved to: {CLEAN_DATA_PATH}")
print(f"Final shape: {df.shape}")
print("\n📊 Columns after cleaning:")
print(df.columns.tolist())
