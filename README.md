# COVID-19-Data-Analysis-Visulization-Project

## Project Summary:
### 1) Data Manipulation and Analysis:
-- Imported necessary libraries such as pandas for data manipulation and analysis.   
--Loaded two CSV files (covid.csv and covid_grouped.csv) into dataframes.

## 2) Data Cleaning:
--Checked for null values and identified columns with missing data.              
--Dropped unnecessary columns (NewCases, NewRecovered, NewDeaths).                 
--Filled missing values in TotalTests with 0 and converted the column to numeric type.         
--Replaced remaining null values in the dataframe with appropriate default values.        

## 3)Data Visualization:
--Created tables using Plotly's create_table.             
--Generated various bar charts and choropleth maps to visualize COVID-19 data:    
  1. -Bar charts to display total cases, deaths, recovered cases, active cases, and tests by 
      country/region.
   2. Choropleth maps for visualizing confirmed, death, and recovered cases globally.          
--Implemented animations to show changes over time.

## 4) Advanced Visualizations:
--Created bubble maps, scatter plots, and word clouds for deeper insights:
  1. Bubble maps to visualize various metrics like total cases, deaths, and recovered cases.
  2. Scatter plots to identify trends and relationships between different COVID-19 metrics.
  3. Word clouds to visualize reasons of death using an additional dataset (covid+death.csv).

## 5) Word Cloud Generation:
--Generated word clouds from the Condition and Condition Group columns to highlight the most 
  common reasons for death related to COVID-19.
