# Impact of Visible Homelessness on Retail Performance 📊

This project analyzes whether visible homelessness in downtown Toronto affects pedestrian foot traffic and monthly retail sales using real-world municipal datasets from 2021–2022 :contentReference[oaicite:0]{index=0}.

## Objective 🎯
To provide a data-driven assessment of the relationship between homelessness levels, pedestrian activity, and retail sales, helping business stakeholders make decisions based on evidence rather than assumptions.

## Data Sources 🗂️
- City of Toronto Open Data
  - Monthly retail sales data
  - Daily shelter usage (homelessness proxy)
  - Daily pedestrian foot-traffic counts

## Methods & Analysis 🛠️
- Data cleaning and transformation across multiple datasets
- Geographic filtering to focus on downtown Toronto
- Conversion of daily data to monthly aggregates
- Median imputation to handle missing pedestrian data
- Exploratory data analysis and time-series visualization
- Multiple linear regression modeling
- Year-based cross-validation (train: 2021, test: 2022)

## Key Findings 🔎
- No statistically significant relationship between homelessness levels and retail sales
- Foot traffic and retail performance are driven primarily by external economic and seasonal factors
- Regression models showed weak predictive power and did not generalize across years

## Tools & Technologies 🛠️
- Python (pandas, numpy, statsmodels)
- City of Toronto Open Data

## Future Improvements 🚀
- Longer time horizon for improved model stability
- Store-level retail sales data
- Additional external variables (events, tourism, economic indicators)
