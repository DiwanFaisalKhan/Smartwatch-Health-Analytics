# Smartwatch Health Data Analysis

Project Overview
For this project, I have collected 30 days of personal health data from my smartwatch.  
The aim was to analyze lifestyle habits and compare them with **WHO-recommended health guidelines** for steps, sleep, and water intake.

Project Workflow

1️.Data Collection
- Exported daily data from smartwatch in CSV format.
- Columns include: Date, Total_Steps, Sleep_Hours, Water_Intake_Liters, Calories_Burned, Heart_Rate, Remarks.

2️.Data Cleaning & EDA (Python and Matplotlib)
- Handled missing values by filling with column means.
- Added goal achievement flags:
  - Steps ≥ 8,000 (WHO recommendation)
  - Sleep ≥ 7 hours
  - Water Intake ≥ 3 liters
- Visualized trends:
  - Daily steps vs WHO benchmark
  - Sleep duration vs recommendation
  - Water intake vs recommendation
- Saved cleaned dataset for further analysis.

3️.SQL Analysis
Key queries used:
-- Average Steps
SELECT AVG(Total_Steps) FROM health_data;

-- Steps goal days
SELECT COUNT(*) FROM health_data WHERE Total_Steps >= 8000;

-- Sleep compliance
SELECT COUNT(*) FROM health_data WHERE Sleep_Hours >= 7;

-- Weekly Average Steps
SELECT 
  DATE_SUB(date, INTERVAL WEEKDAY(date) DAY) AS week_start,
  AVG(total_steps) AS weekly_avg
FROM health_data
GROUP BY week_start
ORDER BY week_start;```

4️.Dashboard Development (Power BI)
1. Main Dashboard
   - Cards: Avg Steps, Avg Sleep Hours, Avg Water Intake, Avg Heart Rate
   - Line charts: Steps & Water intake trends with WHO benchmarks
   - Bar chart: Sleep hours with benchmark
   - Donut/Pie: Remarks distribution
   - Conditional formatting for Steps and Remarks
2. Drillthrough Page
   - Detailed daily breakdown
   - Goal compliance indicators (Yes/No)
   - Contextual remarks

Bookmarks:
- Default View (no filters)
- WHO Goals Achieved (days meeting steps, sleep, and hydration criteria)
- Low Activity Days (steps ≤ 4000)

5️.DAX Formulas
-- Avg Steps
Avg Steps = AVERAGE(health_data[Total_Steps])

-- Steps Goal %
Steps Goal % = DIVIDE(
    COUNTROWS(FILTER(health_data, health_data[Total_Steps] >= 8000)),
    COUNTROWS(health_data),
    0
) * 100

-- Avg Sleep
Avg Sleep = AVERAGE(health_data[Sleep_Hours])

-- Sleep Goal %
Sleep Goal % = DIVIDE(
    COUNTROWS(FILTER(health_data, health_data[Sleep_Hours] >= 7)),
    COUNTROWS(health_data),
    0
) * 100

-- Avg Water Intake
Avg Water Intake = AVERAGE(health_data[Water_Intake_Liters])

-- Hydration Goal %
Hydration Goal % = DIVIDE(
    COUNTROWS(FILTER(health_data, health_data[Water_Intake_Liters] >= 3)),
    COUNTROWS(health_data),
    0
) * 100

-- Most Active Summary
Most Active Summary = 
VAR maxSteps = MAX('smart_watch_health_data'[Total_Steps])
VAR dateOfMax = 
    CALCULATE(
        MAX('smart_watch_health_data'[Date]),
        FILTER(
            'smart_watch_health_data',
            'smart_watch_health_data'[Total_Steps] = maxSteps
        )
    )
RETURN 
    "Most Active: " & FORMAT(dateOfMax, "dd-MMM") & " – " & FORMAT(maxSteps, "#,0") & " steps"

-- Least Active Summary
Least Active Summary = 
VAR minSteps = MIN('smart_watch_health_data'[Total_Steps])
VAR dateOfMin = 
    CALCULATE(
        MAX('smart_watch_health_data'[Date]),
        FILTER(
            'smart_watch_health_data',
            'smart_watch_health_data'[Total_Steps] = minSteps
        )
    )
RETURN 
    "Least Active: " & FORMAT(dateOfMin, "dd-MMM") & " – " & FORMAT(minSteps, "#,0") & " steps"
```

6️.Key Insights
- Steps Goal: Met on 20 out of 30 days (66.7%)
- Sleep Goal: Average 6.9 hours (slightly below recommendation)
- Hydration Goal: Achieved ~70% of days
- Most Active Day: 30-Jul (9,500 steps)
- Least Active Day: 27-Jul (2,253 steps)

7️.Tools & Skills Used
- Python (Pandas, Matplotlib)
- SQL (Aggregation, date functions, compliance tracking)
- Power BI (Interactive dashboard, DAX, drillthrough, bookmarks)
- GitHub (Project hosting & documentation)

Power BI Dashboard: [Download smartwatch_dashboard.pbix](PowerBI/smartwatch_dashboard.pbix) and open in Power BI Desktop.

Closing Statement:
This project demonstrates an end-to-end analytics pipeline, turning raw personal health data into actionable insights using Python, SQL, and Power BI.
Feel free to give suggestions on my email.

