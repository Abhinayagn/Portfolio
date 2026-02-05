# Food Price Inflation Analysis

## Goal

To analyze USDA Consumer Price Index (CPI) and Producer Price Index (PPI) data to identify price trends, volatility patterns, and forecast future changes across food categories from 2020-2026.

## Key Questions

1. Which food categories (meat, dairy, produce, grains) experienced the highest price increases from 2020-2025?
2. How does food price volatility differ between grocery stores and restaurants over the past 5 years?
3. Can we identify seasonal patterns in food price changes that could help consumers time their purchases?
4. What is the correlation between farm-level prices (PPI) and consumer retail prices (CPI)?
5. What actionable recommendations can help households reduce food spending by 10-15%?

## Tools & Technologies

SQL, Python (pandas, numpy, matplotlib), Excel, Tableau or Power BI

## Dataset

**Source:** USDA Economic Research Service - Food Price Outlook

**Time Period:** 1974-2026 (focus on 2020-2026 for main analysis)

**Data Types:** Consumer Price Index (CPI), Producer Price Index (PPI)

**Update Frequency:** Monthly

## Project Status

**Current Progress:** Week 1 Complete

**Data Cleaning:**
- Loaded and transformed USDA CPI data (WIDE to LONG format)
- Cleaned 1,100+ records across 22 food categories, 51 years
- Created processed dataset

**Statistical Analysis:**
- Decade grouping analysis (1970s highest inflation: 8.79%, 2010s lowest: 1.47%)
- Volatility rankings (Eggs most volatile: 10.70%)
- Crisis comparison (2020s inflation 42.4% less severe than 1970s)
- Home vs restaurant analysis (Home cooking 17% cheaper)
- Extreme event detection

**Key Finding:** 2020s food inflation shows 51% lower volatility than 1970s, indicating more resilient modern supply chains.

**Next Steps:** SQL database creation and data visualizations
