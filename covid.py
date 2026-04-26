import pandas as pd

# Load dataset
df = pd.read_csv("covid_vaccine_statewise.csv")

# Display first 5 rows
print("Dataset Preview:\n")
print(df.head())

# -----------------------------
# a. Dataset Description
# -----------------------------
print("\nDataset Info:\n")
print(df.info())

print("\nStatistical Summary:\n")
print(df.describe())

# -----------------------------
# b. First Dose State-wise
# -----------------------------
first_dose = df.groupby("State")["First Dose Administered"].max()

print("\nFirst Dose Vaccination (State-wise):\n")
print(first_dose)

# -----------------------------
# c. Second Dose State-wise
# -----------------------------
second_dose = df.groupby("State")["Second Dose Administered"].max()

print("\nSecond Dose Vaccination (State-wise):\n")
print(second_dose)

# -----------------------------
# d. Total Males Vaccinated
# -----------------------------
male_vaccinated = df.groupby("State")["Male(Individuals Vaccinated)"].max().sum()

print("\nTotal Males Vaccinated:\n", male_vaccinated)

# -----------------------------
# e. Total Females Vaccinated
# -----------------------------
female_vaccinated = df.groupby("State")["Female(Individuals Vaccinated)"].max().sum()

print("\nTotal Females Vaccinated:\n", female_vaccinated)

