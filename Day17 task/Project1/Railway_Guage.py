#Railway Guage

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# SCENARIO 1: BASIC DATA LOADING & CLEANING

# Load dataset using your file path
df = pd.read_csv(r"C:\Users\narah\Downloads\railway_gauges 1.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display column names
print("\nColumn Names:")
print(df.columns)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Replace missing values with 0
df.fillna(0, inplace=True)

# Convert gauge columns to numeric
gauge_cols = ["Broad Gauge", "Metre Gauge", "Narrow Gauge", "Total"]

for col in gauge_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df.head())


# SCENARIO 2: SIMPLE VISUALIZATION - LINE GRAPH

# Extract Year and Total columns
year = df["Year"]
total = df["Total"]

# Plot line graph
plt.figure(figsize=(12, 6))

plt.plot(year, total, marker="o", color="blue")

# Add title and labels
plt.title("Total Railway Track Growth Over Years")
plt.xlabel("Year")
plt.ylabel("Total Railway Track Length")

plt.xticks(rotation=90)
plt.grid(True)

plt.tight_layout()
plt.show()

# Identify trend
if total.iloc[-1] > total.iloc[0]:
    print("\nOverall Trend: Increasing")
elif total.iloc[-1] < total.iloc[0]:
    print("\nOverall Trend: Decreasing")
else:
    print("\nOverall Trend: No Change")


# SCENARIO 3: FILTERING + GROUPED BAR CHART

# Extract starting year
df["Year_Start"] = df["Year"].str[:4].astype(int)

# Filter years after 2000
recent = df[df["Year_Start"] > 2000]

# Select gauge columns
gauges = ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]

# Plot grouped bar chart
recent.plot(
    x="Year",
    y=gauges,
    kind="bar",
    figsize=(14, 6)
)

# Add title and labels
plt.title("Railway Gauge Comparison After 2000")
plt.xlabel("Year")
plt.ylabel("Track Length")

plt.legend(title="Gauge Type")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Identify dominant gauge
print("\nDominant Gauge After 2000:")
print(recent[gauges].sum().idxmax())


# SCENARIO 4: FEATURE ENGINEERING + PIE CHART

# Calculate total sum of each gauge across all years
gauge_totals = df[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].sum()

# Create Series
print("\nGauge Totals:")
print(gauge_totals)

# Plot pie chart
plt.figure(figsize=(8, 8))

plt.pie(
    gauge_totals,
    labels=gauge_totals.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Contribution of Railway Gauge Types")
plt.show()

# Identify gauge with highest contribution
print("\nGauge With Highest Contribution:")
print(gauge_totals.idxmax())

print("\nHighest Total:")
print(gauge_totals.max())


# SCENARIO 5: ADVANCED ANALYSIS + MULTIPLE GRAPHS

# 1. FEATURE ENGINEERING - PERCENTAGE COLUMNS

df["% Broad Gauge"] = (
    df["Broad Gauge"] / df["Total"] * 100
)

df["% Metre Gauge"] = (
    df["Metre Gauge"] / df["Total"] * 100
)

df["% Narrow Gauge"] = (
    df["Narrow Gauge"] / df["Total"] * 100
)

print("\nPercentage Columns:")
print(df[[
    "Year",
    "% Broad Gauge",
    "% Metre Gauge",
    "% Narrow Gauge"
]].head())


# 2. YEARLY GROWTH USING NUMPY np.diff()

growth = np.diff(df["Total"])

# Add first value as 0
df["Yearly Growth"] = np.insert(growth, 0, 0)

print("\nYearly Growth:")
print(df[["Year", "Total", "Yearly Growth"]])


# 3. LINE GRAPH FOR ALL GAUGES

plt.figure(figsize=(12, 6))

plt.plot(
    df["Year"],
    df["Broad Gauge"],
    marker="o",
    label="Broad Gauge"
)

plt.plot(
    df["Year"],
    df["Metre Gauge"],
    marker="o",
    label="Metre Gauge"
)

plt.plot(
    df["Year"],
    df["Narrow Gauge"],
    marker="o",
    label="Narrow Gauge"
)

plt.title("Railway Gauge Trends Over Years")
plt.xlabel("Year")
plt.ylabel("Track Length")

plt.legend()
plt.xticks(rotation=90)
plt.grid(True)

plt.tight_layout()
plt.show()


# 4. STACKED BAR CHART

df.plot(
    x="Year",
    y=["Broad Gauge", "Metre Gauge", "Narrow Gauge"],
    kind="bar",
    stacked=True,
    figsize=(14, 6)
)

plt.title("Railway Gauge Composition Over Years")
plt.xlabel("Year")
plt.ylabel("Track Length")

plt.legend(title="Gauge Type")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()


# 5. IDENTIFY HIGHEST GROWTH YEAR

max_growth = df["Yearly Growth"].max()

max_growth_year = df.loc[
    df["Yearly Growth"].idxmax(), "Year"
]

print("\nHighest Growth:")
print(max_growth)

print("Highest Growth Year:")
print(max_growth_year)


# 6. IDENTIFY MAXIMUM DECLINE

min_growth = df["Yearly Growth"].min()

min_growth_year = df.loc[
    df["Yearly Growth"].idxmin(), "Year"
]

print("\nMaximum Decline:")
print(min_growth)

print("Decline Year:")
print(min_growth_year)


# 7. CHECK DECLINE IN EACH GAUGE

print("\nBroad Gauge Yearly Change:")
print(df["Broad Gauge"].diff())

print("\nMetre Gauge Yearly Change:")
print(df["Metre Gauge"].diff())

print("\nNarrow Gauge Yearly Change:")
print(df["Narrow Gauge"].diff())


# 8. FINAL CONCLUSION

print("\n========== FINAL CONCLUSION ==========")

print("Broad Gauge Total:", df["Broad Gauge"].sum())
print("Metre Gauge Total:", df["Metre Gauge"].sum())
print("Narrow Gauge Total:", df["Narrow Gauge"].sum())

if df["Broad Gauge"].iloc[-1] > df["Broad Gauge"].iloc[0]:
    print("\nBroad Gauge has increased over the years.")

if df["Metre Gauge"].iloc[-1] < df["Metre Gauge"].iloc[0]:
    print("Metre Gauge has decreased over the years.")

if df["Narrow Gauge"].iloc[-1] < df["Narrow Gauge"].iloc[0]:
    print("Narrow Gauge has decreased over the years.")

print("\nConclusion:")
print("The railway system is shifting towards Broad Gauge dominance.")
print("Broad Gauge contributes the largest share of railway tracks.")
print("Metre Gauge and Narrow Gauge have smaller contributions.")
