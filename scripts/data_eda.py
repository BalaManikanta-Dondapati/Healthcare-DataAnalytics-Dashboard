import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


#  Load Cleaned Dataset

CLEAN_DATA_PATH = os.path.join("data", "processed", "hospital_cleaned.csv")
df = pd.read_csv(CLEAN_DATA_PATH, low_memory=False)
print("🔹 Loading cleaned dataset...")

print("✅ Dataset loaded successfully! Shape:", df.shape)

# Convert Mixed-Type Columns to Numeric

df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce')
df['Total Costs'] = pd.to_numeric(df['Total Costs'], errors='coerce')
df['Length of Stay'] = pd.to_numeric(df['Length of Stay'], errors='coerce')

# Drop rows with missing essential numeric data (optional)
df = df.dropna(subset=['Total Charges', 'Total Costs'])


#  Descriptive Statistics

print("\n📊 Descriptive Statistics:")
print(df[['Total Charges', 'Total Costs', 'Length of Stay']].describe())


#  Most Common Diagnoses

top_diagnoses = df['CCS Diagnosis Description'].value_counts().head(10)
print("\n🏥 Top 10 Diagnoses by Frequency:")
print(top_diagnoses)

# Save plot
plt.figure(figsize=(10, 6))
sns.barplot(
    y=top_diagnoses.index,
    x=top_diagnoses.values,
    hue=top_diagnoses.index,  # fixes deprecation warning
    dodge=False,
    legend=False,
    palette="coolwarm"
)
plt.title("Top 10 Diagnoses by Frequency")
plt.xlabel("Number of Cases")
plt.ylabel("Diagnosis")
plt.tight_layout()
os.makedirs("reports/figures", exist_ok=True)
plt.savefig("reports/figures/top_diagnoses.png")
print("📈 Saved: top_diagnoses.png")


# 5Average Cost and Charges by Diagnosis

avg_costs = (
    df.groupby('CCS Diagnosis Description')[['Total Charges', 'Total Costs']]
    .mean()
    .sort_values(by='Total Charges', ascending=False)
    .head(10)
)
print("\n💰 Top 10 Diagnoses by Average Total Charges:")
print(avg_costs)

plt.figure(figsize=(10, 6))
sns.barplot(
    y=avg_costs.index,
    x=avg_costs['Total Charges'],
    hue=avg_costs.index,
    dodge=False,
    legend=False,
    palette="viridis"
)
plt.title("Top 10 Diagnoses by Average Total Charges")
plt.xlabel("Average Total Charges ($)")
plt.ylabel("Diagnosis")
plt.tight_layout()
plt.savefig("reports/figures/avg_charges_by_diagnosis.png")
print("📈 Saved: avg_charges_by_diagnosis.png")


# Distribution of Total Charges

plt.figure(figsize=(8, 5))
sns.histplot(df['Total Charges'], bins=50, kde=True, color="skyblue")
plt.title("Distribution of Total Charges")
plt.xlabel("Total Charges ($)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("reports/figures/distribution_total_charges.png")
print("📈 Saved: distribution_total_charges.png")


# Average Length of Stay by Severity

avg_stay = (
    df.groupby('APR Severity of Illness Description')['Length of Stay']
    .mean()
    .sort_values(ascending=False)
)
print("\n🩺 Average Length of Stay by Severity of Illness:")
print(avg_stay)

plt.figure(figsize=(8, 5))
sns.barplot(
    x=avg_stay.values,
    y=avg_stay.index,
    hue=avg_stay.index,
    dodge=False,
    legend=False,
    palette="magma"
)
plt.title("Average Length of Stay by Severity of Illness")
plt.xlabel("Average Days")
plt.ylabel("Severity Level")
plt.tight_layout()
plt.savefig("reports/figures/avg_stay_by_severity.png")
print("📈 Saved: avg_stay_by_severity.png")


# Cost Comparison: Emergency vs Non-Emergency

emergency_cost = (
    df.groupby('Emergency Department Indicator')['Total Charges']
    .mean()
    .sort_index()
)
print("\n🚑 Average Total Charges (Emergency vs Non-Emergency):")
print(emergency_cost)

plt.figure(figsize=(6, 4))
sns.barplot(
    x=emergency_cost.index,
    y=emergency_cost.values,
    hue=emergency_cost.index,
    dodge=False,
    legend=False,
    palette=["#FF6B6B", "#4D96FF"]
)
plt.title("Average Total Charges: Emergency vs Non-Emergency")
plt.xlabel("Emergency Department Indicator")
plt.ylabel("Average Total Charges ($)")
plt.tight_layout()
plt.savefig("reports/figures/emergency_vs_non_emergency.png")
print("📈 Saved: emergency_vs_non_emergency.png")


# Save EDA Summary

eda_summary = pd.DataFrame({
    "Top Diagnoses": top_diagnoses,
    "Avg Charges by Diagnosis": avg_costs['Total Charges']
})
summary_path = os.path.join("data", "processed", "eda_summary.csv")
eda_summary.to_csv(summary_path)
print(f"\n📊 EDA Summary saved to: {summary_path}")

print("\n✅ EDA completed successfully!")
