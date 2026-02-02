# Power BI Sales Analytics Workshop

## Title: Power BI Sales Analytics Dashboard

**Goal:** To develop proficiency in Power BI for creating interactive business intelligence dashboards that transform raw sales data into actionable insights for data-driven decision-making.

**Description:** This project was completed as part of a comprehensive Power BI workshop conducted by Akhilesh Meena, Founder at Datacense and Business Intelligence & Analytics strategist. The workshop focused on building end-to-end analytics solutions using Power BI, covering the complete workflow from data preparation to dashboard creation and visualization.

The dataset consisted of sales transaction data from a retail business across Middle Eastern markets (UAE, Oman, Qatar, Bahrain, Kuwait, and India) spanning 2023-2024. The data included 2,746 sales records with attributes such as invoice date, location, country, sales managers, salesmen, customers, customer types (Supermarkets, Hypermarkets, Hotels, Groceries & Shops), products, sales amounts, costs, and profit margins.

The project involved connecting to data sources, performing data transformation and cleaning in Power Query Editor, establishing relationships in the data model, creating calculated columns and measures using DAX (Data Analysis Expressions), and designing interactive visualizations. The dashboard provides comprehensive insights into sales performance across multiple dimensions including geographical distribution, customer segmentation, product performance, and temporal trends.

**Skills:** Data connection and import, Power Query transformations, data modeling, DAX formulas, data visualization, dashboard design, interactive filtering, KPI development, business intelligence, sales analytics.

**Technology:** Power BI Desktop, Power Query, DAX (Data Analysis Expressions), Excel (data source).

**Results:** Successfully created an interactive Sales Analytics Dashboard featuring:

**Key Performance Indicators (Top Center):**
- Total Profit: 49M
- Total Sales: 89M  
- Total Cost: 40M

**Six Comprehensive Visualizations:**

1. **Sale by Country** (Horizontal Bar Chart - Top Left)
   - India leads with approximately 40M in sales
   - UAE follows with around 29M
   - Oman contributes approximately 11M
   - Qatar, Bahrain, and Kuwait show smaller but significant contributions
   - Clear visual hierarchy showing market dominance

2. **Sale by Cust_Type** (Donut Chart - Top Center)
   - Supermarkets: 56.18% (50M) - dominant customer segment
   - Hypermarkets: 20.83% (18M)
   - Hotels: 20.73% (18M)  
   - Groceries & Shops: 2.26% (2M)
   - Color-coded for easy segment identification

3. **Customer Details Table** (Top Right)
   - Displays Sale, Customer, and Profit columns
   - Shows top customers including Carrefour (8.4M sales, 4.7M profit)
   - Chelsea 2 (1.3M sales, 738K profit)
   - Big Mart (79K sales, 23K profit)
   - Total: 89,167,157 in sales and 49,138,247 in profit
   - Enables drill-down to individual customer performance

4. **Sale by Sales_Manager** (Column Chart - Bottom Left)
   - Compares performance across 13+ sales managers
   - Top performers showing 10M+ in sales
   - Clear performance distribution from highest to lowest
   - Identifies top contributors and potential coaching opportunities

5. **Sale by Product** (Horizontal Bar Chart - Bottom Center)
   - 330 ml leads as top product with highest sales
   - 450 L-Mint, 200 ml-24, 1L Reg-12 follow in descending order
   - Lemon 500, Partner C-Top, and other products shown
   - Ranges from 40M+ for top product to minimal sales for lowest items
   - Supports inventory and product strategy decisions

6. **Sale by Quarter** (Column Chart - Bottom Right)
   - Quarterly trend analysis showing sales performance
   - Qtr 1 and Qtr 2 showing strong performance around 20M each
   - Qtr 3 and Qtr 4 showing consistent performance
   - Enables seasonal pattern identification and forecasting

**Dashboard Design Excellence:**
- Clean, professional layout with mustard/gold color scheme
- Consistent visual hierarchy and alignment
- Effective use of white space
- Clear axis labels and data labels
- Interactive cross-filtering across all visualizations
- Professional title header "Overview"
- Responsive design suitable for different screen sizes

The dashboard demonstrates proficiency in Power BI's core capabilities including data modeling, DAX calculations, visual selection, formatting, and creating a cohesive business intelligence solution that transforms raw transactional data into actionable insights for sales strategy, customer targeting, and performance management.

---

## Workshop Information

**Workshop Conducted By:** Akhilesh Meena  
**Title:** Founder | Business Intelligence & Analytics | Data Automation Strategist | Corporate Trainer | Power BI | Microsoft Excel  
**Organization:** Datacense  
**LinkedIn:** [Akhilesh Meena](https://www.linkedin.com/in/akhileshmeena/)

**Key Learning Outcomes:**
- Power BI interface navigation and workspace setup
- Data import from multiple sources (Excel, CSV, databases)
- Power Query Editor for data transformation and cleaning
- Data modeling and relationship establishment
- DAX fundamentals for calculated columns and measures
- Visualization types and their appropriate use cases
- Dashboard design principles and best practices
- Interactive filtering with slicers and cross-filtering
- Publishing and sharing dashboards

---

## Dashboard Features

### 1. **KPI Cards (Top Section)**
- Total Profit: 49M
- Total Sales: 89M
- Total Cost: 40M
- Prominently displayed for at-a-glance performance monitoring

### 2. **Geographic Analysis**
- Horizontal bar chart: Sales by Country
- Six markets visualized (India, UAE, Oman, Qatar, Bahrain, Kuwait)
- India clearly leading with 40M

### 3. **Customer Segmentation**
- Donut chart: Sales by Customer Type
- Four segments: Supermarkets (56.18%), Hypermarkets (20.83%), Hotels (20.73%), Groceries & Shops (2.26%)
- Color-coded for easy interpretation

### 4. **Customer Performance Table**
- Detailed breakdown by customer name
- Shows Sales, Customer, and Profit columns
- Total sales: 89,167,157 | Total profit: 49,138,247
- Top customers: Carrefour, Chelsea 2, Big Mart, and others

### 5. **Product Analysis**
- Horizontal bar chart: Sales by Product
- 12+ product lines displayed
- 330 ml leading product performance
- Range from high-volume to specialty products

### 6. **Sales Team Performance**
- Column chart: Sales by Sales_Manager
- 13+ sales managers compared
- Performance range from 10M+ to minimal contributions
- Enables performance benchmarking

### 7. **Temporal Analysis**
- Column chart: Sales by Quarter
- Four quarters displayed
- Consistent performance across periods
- Quarterly comparison capabilities

### 8. **Interactive Features**
- Cross-filtering enabled across all visualizations
- Click any chart element to filter entire dashboard
- Drill-through capabilities for detailed analysis
- Clean, professional mustard/gold color scheme

---

## Key Insights

1. **Market Leadership:** India dominates with approximately 40M in sales, representing 45% of total revenue
2. **Customer Concentration:** Supermarkets are the primary revenue driver at 56.18% (50M), making them critical for business success
3. **Top Product Performance:** 330 ml product line is the best-seller, driving significant sales volume
4. **High-Value Customers:** Carrefour leads customer profitability with 8.4M in sales and 4.7M in profit
5. **Healthy Margins:** Overall profit margin of 55% (49M profit on 89M sales) indicates strong pricing and cost management
6. **Consistent Quarterly Performance:** All quarters show 15M+ in sales, indicating stable business operations
7. **Sales Team Performance:** Wide performance distribution across sales managers suggests opportunity for knowledge sharing and standardization of best practices

---

## Technical Highlights

- **Data Preparation:** Imported and transformed 2,746 sales records with 11 fields using Power Query Editor
- **Data Modeling:** Structured data relationships for optimal query performance
- **DAX Measures:** Created calculated measures including:
  - Total Sales = SUM(Transactions[Sale])
  - Total Cost = SUM(Transactions[Cost])
  - Total Profit = SUM(Transactions[Profit])
  - Profit Margin calculations
- **Visualizations:** Implemented 7 different visualization types:
  - KPI Cards (3)
  - Horizontal Bar Charts (2)
  - Donut Chart (1)
  - Column Charts (2)
  - Table visualization (1)
- **Color Scheme:** Professional mustard/gold theme with high contrast for readability
- **Layout Design:** Grid-based layout ensuring visual balance and hierarchy
- **Interactivity:** Cross-filtering enabled across all 6 main visualizations
- **Performance:** Optimized for quick loading and responsive filtering
- **Formatting:** Consistent axis labels, data labels, and tooltips throughout

---



## Acknowledgments

Special thanks to **Akhilesh Meena** for conducting an excellent workshop that provided hands-on experience with Power BI and practical insights into business intelligence dashboard development. The workshop's structured approach to teaching Power BI fundamentals, combined with real-world datasets and business scenarios, made it an invaluable learning experience.


