# Power BI Dashboard Build Guide

Use this guide to recreate the dashboard in Power BI.

## Data Source

Load this file:

```text
data/processed/fpna_kpi_summary.csv
```

## Recommended Dashboard Pages

### Page 1: Financial Overview

Cards:
- Actual Revenue
- Revenue Variance
- Operating Profit
- Operating Margin

Charts:
- Line chart: Month vs Revenue_Budget and Revenue_Actual
- Bar chart: Month vs Operating_Profit_Actual
- KPI card: Revenue_Variance_Pct

### Page 2: Budget vs Actual Variance

Charts:
- Clustered bar chart: Month vs Revenue_Variance
- Clustered bar chart: Month vs Profit_Variance
- Table: Month, Driver_Notes, Revenue_Variance, Profit_Variance

### Page 3: Expense Analysis

Charts:
- Clustered bar chart: expense category budget vs actual
- Donut chart: actual opex mix
- Table: controllable expenses with variance comments

### Page 4: Forecast

Use the Excel workbook Forecast sheet or create forecast measures in Power BI.

## Suggested DAX Measures

```DAX
Total Revenue Actual = SUM(fpna_kpi_summary[Revenue_Actual])
Total Revenue Budget = SUM(fpna_kpi_summary[Revenue_Budget])
Revenue Variance = [Total Revenue Actual] - [Total Revenue Budget]
Revenue Variance % = DIVIDE([Revenue Variance], [Total Revenue Budget])

Operating Profit Actual = SUM(fpna_kpi_summary[Operating_Profit_Actual])
Operating Profit Budget = SUM(fpna_kpi_summary[Operating_Profit_Budget])
Profit Variance = [Operating Profit Actual] - [Operating Profit Budget]
Operating Margin = DIVIDE([Operating Profit Actual], [Total Revenue Actual])
```
