import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load job data from the provided CSV file
csv_path = r"C:\Users\Kelley\Documents\GitHub\data_analysis\getting_started\postings.csv"
df = pd.read_csv(csv_path)

# Selecting relevant columns
df = df[["title", "company_name", "location", "max_salary", "skills_desc"]]
df.columns = ["Job Title", "Company", "Location", "Salary", "Skills"]

# Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(subset=["Job Title", "Salary", "Skills"], inplace=True)

def clean_salary(s):
    if pd.isna(s):
        return np.nan
    return float(s)

df["Salary"] = df["Salary"].apply(clean_salary)

df["Skills"] = df["Skills"].fillna("No Skills Listed").str.split(",")
skills_df = df.explode("Skills")
top_skills = skills_df["Skills"].value_counts().head(10)

# Salary trends by job title
salary_trends = df.groupby("Job Title")["Salary"].mean().sort_values(ascending=False)

# Job openings by location
job_locations = df["Location"].value_counts().head(10)

# Visualization
plt.figure(figsize=(10,5))
sns.barplot(x=top_skills.index, y=top_skills.values, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Top 10 In-Demand Skills")
plt.xlabel("Skills")
plt.ylabel("Job Count")
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(df["Salary"].dropna(), bins=20, kde=True)
plt.title("Salary Distribution")
plt.xlabel("Salary ($)")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(10,5))
sns.barplot(x=job_locations.index, y=job_locations.values, palette="viridis")
plt.xticks(rotation=45)
plt.title("Top 10 Job Locations")
plt.xlabel("Location")
plt.ylabel("Job Openings")
plt.show()

print("Job Market Analysis Complete!")
