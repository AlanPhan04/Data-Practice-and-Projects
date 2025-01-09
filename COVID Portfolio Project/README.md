# COVID-19 Portfolio Project

## Overview
This project explores and analyzes COVID-19 data using SQL. It is designed as a portfolio project to showcase SQL skills such as data retrieval, aggregation, transformation, and filtering to extract meaningful insights. The dataset used includes global COVID-19 statistics, such as total cases, new cases, total deaths, and population data, categorized by country and continent.

## Dataset
The dataset includes the following columns:
- **Location**: The country or region.
- **Date**: The date of the recorded data.
- **Total Cases**: Cumulative number of confirmed COVID-19 cases.
- **New Cases**: Number of new cases recorded on the specified date.
- **Total Deaths**: Cumulative number of confirmed COVID-19 deaths.
- **Population**: Total population of the country or region.

## Project Objectives
The primary goals of this project are to:
1. Analyze trends in COVID-19 data across different countries and continents.
2. Calculate metrics such as the death rate and new case rate.
3. Identify patterns or anomalies in the dataset.
4. Use SQL to answer specific analytical questions about the pandemic.

## SQL Queries
### 1. Data Selection and Cleaning
The project begins by selecting and organizing the dataset, ensuring columns like `continent` are not null:
```sql
SELECT *
FROM COVIDDEATH
WHERE CONTINENT IS NOT NULL
ORDER BY LOCATION, DATEE;
```

### 2. Exploring Total Cases and Deaths
To analyze the cumulative cases and deaths for each country:
```sql
SELECT LOCATION
    , DATEE
    , COALESCE(TOTAL_CASES, 0) AS TOTAL_CASES
    , COALESCE(TOTAL_DEATHS, 0) AS TOTAL_DEATHS
    , COALESCE(ROUND(TOTAL_DEATHS/TOTAL_CASES * 100, 2), 0) AS DEATH_RATE
FROM COVIDDEATH
ORDER BY LOCATION, DATEE;
```

### 3. Analyzing Population Impact
To calculate the infection rate as a percentage of the population:
```sql
SELECT LOCATION
    , DATEE
    , POPULATION
    , COALESCE(TOTAL_CASES, 0) AS TOTAL_CASES
    , COALESCE(ROUND(TOTAL_CASES/POPULATION * 100, 2), 0) AS INFECTION_RATE
FROM COVIDDEATH
WHERE POPULATION IS NOT NULL
ORDER BY LOCATION, DATEE;
```

### 4. Insights by Continent
To summarize data by continent and calculate total and average metrics:
```sql
SELECT CONTINENT
    , COALESCE(SUM(NEW_CASES), 0) AS TOTAL_NEW_CASES
    , COALESCE(SUM(NEW_DEATHS), 0) AS TOTAL_NEW_DEATHS
    , COALESCE(ROUND(AVG(NEW_CASES), 2), 0) AS AVG_NEW_CASES
    , COALESCE(ROUND(AVG(NEW_DEATHS), 2), 0) AS AVG_NEW_DEATHS
FROM COVIDDEATH
GROUP BY CONTINENT
ORDER BY CONTINENT;
```

### 5. Country-Specific Analysis
To focus on specific countries:
```sql
SELECT LOCATION
    , DATEE
    , NEW_CASES
    , NEW_DEATHS
    , ROUND(NEW_DEATHS/NEW_CASES * 100, 2) AS DEATH_RATE
FROM COVIDDEATH
WHERE LOCATION IN ('India', 'United States', 'Brazil')
ORDER BY LOCATION, DATEE;
```

## Tools
- **SQL**: For writing and executing queries.
- **Database Management System**: Any SQL-compatible tool (e.g., MySQL, PostgreSQL, or SQLite).

## Results
The queries provide insights into the global impact of COVID-19, such as:
- Trends in total cases and deaths over time.
- Variations in infection and death rates across countries and continents.
- Population-level insights into the spread of the virus.

## How to Use
1. Clone this repository.
2. Import the dataset into your SQL database.
3. Run the provided SQL queries to explore and analyze the data.

## Future Enhancements
- Include visualizations to better interpret the data.
- Automate data retrieval and cleaning processes.
- Add more granular insights, such as vaccination data.

## Author
This project was created as part of a portfolio to demonstrate SQL skills and data analysis expertise. Feedback and contributions are welcome!

