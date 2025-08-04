-- Average Steps
SELECT AVG(Total_Steps) AS Avg_Steps FROM health_data;

-- Days ≥ 8000 steps
SELECT COUNT(*) AS Goal_Days
FROM health_data
WHERE Total_Steps >= 8000;

-- Sleep Compliance
SELECT COUNT(*) AS Good_Sleep_Days
FROM health_data
WHERE Sleep_Hours >= 7;

-- Hydration Compliance
SELECT COUNT(*) AS Good_Hydration_Days
FROM health_data
WHERE Water_Intake_Liters >= 3;

-- Weekly Average Steps
SELECT 
  DATE_SUB(date, INTERVAL WEEKDAY(date) DAY) AS week_start,
  AVG(total_steps) AS weekly_avg
FROM health_data
GROUP BY week_start
ORDER BY week_start;
