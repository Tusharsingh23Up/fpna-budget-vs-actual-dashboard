from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "fpna_kpi_summary.csv"

st.set_page_config(page_title="FP&A Budget vs Actual Dashboard", layout="wide")

st.title("FP&A Budget vs Actual Variance Dashboard")
st.caption("Portfolio project for Financial Analyst / FP&A roles")

df = pd.read_csv(DATA_PATH)

total_budget_revenue = df["Revenue_Budget"].sum()
total_actual_revenue = df["Revenue_Actual"].sum()
revenue_variance = total_actual_revenue - total_budget_revenue
total_actual_profit = df["Operating_Profit_Actual"].sum()
total_budget_profit = df["Operating_Profit_Budget"].sum()
profit_variance = total_actual_profit - total_budget_profit
operating_margin = total_actual_profit / total_actual_revenue

col1, col2, col3, col4 = st.columns(4)
col1.metric("FY2025 Actual Revenue", f"${total_actual_revenue/1000:,.0f}k", f"{revenue_variance/1000:,.0f}k vs budget")
col2.metric("Operating Profit", f"${total_actual_profit/1000:,.0f}k", f"{profit_variance/1000:,.0f}k vs budget")
col3.metric("Operating Margin", f"{operating_margin:.1%}")
col4.metric("Revenue Variance %", f"{revenue_variance/total_budget_revenue:.1%}")

st.subheader("Revenue: Budget vs Actual")
revenue_long = df.melt(
    id_vars=["Month_Name"],
    value_vars=["Revenue_Budget", "Revenue_Actual"],
    var_name="Metric",
    value_name="Revenue"
)
fig_revenue = px.line(revenue_long, x="Month_Name", y="Revenue", color="Metric", markers=True)
st.plotly_chart(fig_revenue, use_container_width=True)

st.subheader("Operating Profit Variance by Month")
fig_profit = px.bar(df, x="Month_Name", y="Profit_Variance")
st.plotly_chart(fig_profit, use_container_width=True)

st.subheader("Expense Analysis")
expense_totals = pd.DataFrame({
    "Category": ["Salaries", "Marketing", "Operations", "Admin"],
    "Budget": [
        df["Salaries_Budget"].sum(),
        df["Marketing_Budget"].sum(),
        df["Operations_Budget"].sum(),
        df["Admin_Budget"].sum(),
    ],
    "Actual": [
        df["Salaries_Actual"].sum(),
        df["Marketing_Actual"].sum(),
        df["Operations_Actual"].sum(),
        df["Admin_Actual"].sum(),
    ],
})
expense_long = expense_totals.melt(id_vars="Category", var_name="Scenario", value_name="Amount")
fig_expense = px.bar(expense_long, x="Category", y="Amount", color="Scenario", barmode="group")
st.plotly_chart(fig_expense, use_container_width=True)

st.subheader("Management Recommendations")
st.write(
    """
    - Keep high-ROI revenue channels active because Q4 demand and upsell campaigns supported positive revenue variance.
    - Review June and September profitability because these months had the weakest profit variance.
    - Tighten approval controls around marketing and hiring-related spend.
    - Use the Excel model to update assumptions and produce best-case, base-case, and worst-case forecasts.
    """
)

st.subheader("Detailed KPI Table")
st.dataframe(df, use_container_width=True)
