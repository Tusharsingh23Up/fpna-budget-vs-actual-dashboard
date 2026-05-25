# FP&A Budget vs Actual Variance Analysis with Forecasting Dashboard

## Project Overview

This end-to-end Financial Analyst / FP&A project analyzes a fictional business unit, **AlphaMart SaaS Division**, using monthly budget vs actual financial data for FY2025. The project identifies revenue and cost variances, explains key business drivers, builds a six-month forecast, and presents executive-level recommendations.

## Business Problem

Management wants to know:

1. Did the business perform above or below budget?
2. Which months created the biggest profit variance?
3. Which expense categories need tighter control?
4. What revenue and operating profit should be expected for the next six months?
5. What actions should management take?

## Files Included

```text
fpna-budget-vs-actual-github/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   │   └── fpna_budget_actual_monthly.csv
│   └── processed/
│       ├── fpna_kpi_summary.csv
│       └── summary_metrics.json
├── models/
│   └── FPNA_Budget_vs_Actual_Model.xlsx
├── src/
│   └── fpna_analysis.py
├── dashboards/
│   ├── streamlit_dashboard.py
│   └── powerbi_build_guide.md
├── reports/
│   ├── executive_summary.md
│   └── project_walkthrough.md
├── docs/
│   ├── data_dictionary.md
│   ├── business_questions.md
│   └── resume_bullets.md
└── images/
    ├── revenue_budget_vs_actual.png
    ├── profit_variance_by_month.png
    ├── actual_opex_by_category.png
    └── dashboard_preview.png
```

## Key Findings

| Metric | Result |
|---|---:|
| FY2025 Budget Revenue | $14,474,470 |
| FY2025 Actual Revenue | $14,634,571 |
| Revenue Variance | $160,101 |
| Revenue Variance % | 1.1% |
| FY2025 Actual Operating Profit | $4,210,653 |
| Operating Profit Variance | $39,311 |
| Actual Operating Margin | 28.8% |
| Best Profit Month | Dec-2025 |
| Weakest Profit Variance Month | Jun-2025 |

## Tools Used

- Microsoft Excel for the financial model, dashboard, formulas, variance analysis, and forecast
- Python for data processing, KPI calculation, and chart generation
- Streamlit for an optional interactive dashboard
- Power BI-ready CSV data and build guide

## How to Run the Python Analysis

```bash
pip install -r requirements.txt
python src/fpna_analysis.py
```

## How to Run the Streamlit Dashboard

```bash
pip install -r requirements.txt
streamlit run dashboards/streamlit_dashboard.py
```

## How to Use the Excel Model

Open:

```text
models/FPNA_Budget_vs_Actual_Model.xlsx
```

Recommended walkthrough order:

1. **How_To_Use**
2. **Assumptions**
3. **Monthly_Data**
4. **Variance_Analysis**
5. **Forecast**
6. **Dashboard**
7. **Sources**

## Resume Project Title

**Financial Performance Analysis: Budget vs Actual Variance and Revenue Forecasting Dashboard**

## Resume Bullet

Built an FP&A dashboard using Excel and Python to analyze FY2025 budget vs actual variance, forecast revenue and operating profit, track profitability KPIs, and recommend cost-control actions that improved executive decision-making.

## Disclaimer

This project uses a synthetic dataset created for educational and portfolio demonstration purposes. It does not use confidential company data.
