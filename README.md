🏥 NY Hospital Inpatient Analytics Dashboard — 2010

📌 Project Overview

This project analyzes New York State Hospital Inpatient Discharge Data (2010) to uncover insights about hospital utilization, patient demographics, treatment costs, and the relationship between severity of illness and healthcare expenses.

Using Power BI for visualization and Python (Pandas) for preprocessing, we’ve built a fully interactive analytical dashboard that empowers healthcare administrators to identify high-cost diagnoses, track performance, and improve hospital efficiency.

🧰 Tools & Technologies

1.Stage	Tools Used

2.Data Cleaning & Preprocessing	Python, Pandas

3.Visualization	Power BI Desktop

4.Environment	VS Code, Power BI Service

5.Dataset Source	Kaggle: 2010 New York State Hospital Inpatient Discharge Data

📊 Dataset Access
Due to GitHub’s 100 MB file limit, the raw and cleaned datasets are hosted externally:

- [🗂️ Raw Hospital Discharge Dataset (Google Drive)](https://drive.google.com/file/d/1vzcb3pT5qGX4dHl1m8VsvyZzH5EZDDE4/view?usp=sharing)
- [🧹 Cleaned Hospital Dataset (Google Drive)](https://drive.google.com/file/d/1tnXg5IZrGpOVpm0TguRQtIpMbkkyGK8E/view?usp=sharing)
- [📈 Power BI Dashboard (.pbix) File (Google Drive)](https://drive.google.com/file/d/15qGd3SM-eOkE-44HKRgBSgp1238Ry2fD/view?usp=sharing)



📂 Folder Structure
```
Healthcare-DataAnalytics-Dashboard/
│
├── data/
│   ├── raw/
│   │   └── hospital-inpatient-discharges.csv(Google Drive Link)
│   └── processed/
│       └── hospital_cleaned.csv(Google Drive Link)
│
├── reports/figures/
│   └── avg_charges_by_diagnosis.png
│   └── avg_stay_by_severity.png
│   └── distribution_total_charges.png
│   └── emergency_vs_non_emergency.png
│   └── top_diagnoses.png
│
├── scripts/
│   └── data_cleaning.py
│   └── data_eda.py
│   └── data_understanding.py
│
├── visuals/
│   ├── Hospital_Analytics_Dashboard.pdf
│   └── Hospital_Analytics_Dashboard.png
│
└── README.md
└── .gitignore
└── requirements.txt


```


🧹 Data Preprocessing Steps

1.Performed in Python (VS Code)

2.Loaded raw dataset using pandas.read_csv().

3.Handled missing values — replaced or dropped irrelevant records.

4.Removed redundant columns and standardized column names.

5.Converted data types (e.g., cost/charge columns → float).

6.Saved cleaned dataset as data/processed/hospital_cleaned.csv.


✅ Final dataset shape: 2,597,840 rows × 33 columns


📊 Dashboard Design in Power BI

🧱 Step 1: Import & Data Model

-->Imported hospital_cleaned.csv

-->Verified data types, created relationships where needed.

🧱 Step 2: Create Calculated Fields

--.Used DAX to create:

Total Charges (bn) = SUM('hospital_cleaned'[Total Charges]) / 1e9

Total Costs (bn) = SUM('hospital_cleaned'[Total Costs]) / 1e9

Average Stay = AVERAGE('hospital_cleaned'[Length of Stay])

🧱 Step 3: Build Visuals
--.No	Visualization	Chart Type	Description
1.KPI Cards	Card	Count of Facility IDs, Total Charges, Total Costs, Avg Length of Stay

2.Top Diagnoses by Facility Count	Column	Most common diagnosis categories

3.Average Charges by Diagnosis	Funnel	Most expensive treatments

4.Avg Charges by Severity	Bar	Cost variation by illness severity

5.Charges vs Length of Stay	Combo	Correlation between charges & stay duration

6.Emergency vs Non-Emergency	Pie	Cost distribution by emergency indicator

7.Age Group & Gender Distribution	Area	Admission trends by age & gender

8.Race-wise Distribution	Donut	Patient demographics by race

9.Charges & Costs by Facility	100% Stacked Bar	Hospital-wise cost comparison

🎛️ Step 4: Interactivity

-->Added slicers for:

1.Discharge Year

2.Facility Name

3.Severity of Illness

4.Emergency Department Indicator

Each slicer dynamically filters all visuals across the report.

Example: selecting a hospital updates all KPIs and charts instantly.

🎨 Step 5: Layout & Styling

-->Title: NY Hospital Inpatient Analytics Dashboard — 2010

1.KPIs placed at the top for summary view

2.Organized visuals into sections:

3.Costs Overview

4.Diagnosis Analysis

5.Severity & Stay Insights

6.Demographic Breakdown

7.Facility Comparison

-->Consistent colors:

🟥 Emergency cases

🟦 Non-Emergency cases

-->Rounded card edges, subtle shadows for modern UI look.

💡 Key Insights

-->Extreme illness severity drives the highest average charges and longest hospital stays.

-->Emergency cases account for nearly 50% of total costs.

-->Age group 50–69 dominates hospital admissions.

-->White race group forms the majority of admitted patients.

A few hospitals contribute disproportionately to total expenditures — scope for cost optimization.

🚀 How to Run

1.Open Power BI Desktop.

2.Load hospital_cleaned.csv.

3.Open Hospital_Analytics_Dashboard.pbix.

4.Refresh the dataset to sync visuals.

5.Export to .pdf or .png for sharing or upload to GitHub Pages.

📸 Dashboard Preview

🏁 Conclusion

This project demonstrates how data-driven insights can improve hospital performance and patient care decisions. It combines Python-based data cleaning and Power BI analytics to create a professional, interactive visualization suited for data analyst portfolios.
