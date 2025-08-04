import pandas as pd
import matplotlib.pyplot as plt

# Loading data in pandas
df = pd.read_csv("../Data/smart_watch_health_data.csv", parse_dates=["Date"], dayfirst=True)

# code for Missing Values Handling 
df["Total_Steps"] = df["Total_Steps"].fillna(df["Total_Steps"].mean())
df["Distance_km"] = df["Distance_km"].fillna(df["Distance_km"].mean())
df["Calories_Burned"] = df["Calories_Burned"].fillna(df["Calories_Burned"].mean())

# Add WHO Goal Flags 
df['Steps_Goal'] = df['Total_Steps'] >= 8000
df['Sleep_Goal'] = df['Sleep_Hours'] >= 7
df['Water_Goal'] = df['Water_Intake_Liters'] >= 3

# Summary Stats 
print("Average Steps:", round(df['Total_Steps'].mean(), 2))
print("Days ≥ 8000 steps:", df['Steps_Goal'].sum(), "of", len(df))
print("Average Sleep Hours:", round(df['Sleep_Hours'].mean(), 2))
print("Days ≥ 7 hrs sleep:", df['Sleep_Goal'].sum())
print("Average Water Intake:", round(df['Water_Intake_Liters'].mean(), 2))
print("Days ≥ 3L water:", df['Water_Goal'].sum())

# Visualization in Matplotlib
plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['Total_Steps'], marker='o', label="Daily Steps")
plt.axhline(8000, linestyle="--", label="WHO Goal (8000)")
plt.title("Daily Steps vs WHO 8000 Steps Benchmark")
plt.xlabel("Date")
plt.ylabel("Steps")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("../Images/steps_trend.png")
plt.close()

plt.figure(figsize=(12,5))
plt.bar(df['Date'], df['Sleep_Hours'])
plt.axhline(7, linestyle="--", label="WHO Goal (7 hrs)")
plt.title("Daily Sleep vs WHO Recommended Hours")
plt.xlabel("Date")
plt.ylabel("Sleep Hours")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("../Images/sleep_chart.png")
plt.close()

plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['Water_Intake_Liters'], marker='o')
plt.axhline(3, linestyle="--", label="Recommended 3L")
plt.title("Daily Water Intake vs Recommended 3L")
plt.xlabel("Date")
plt.ylabel("Water Intake (Liters)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("../Images/water_intake.png")
plt.close()

# Save cleaned data for reuse
df.to_csv("../Data/cleaned_smartwatch_data.csv", index=False)
