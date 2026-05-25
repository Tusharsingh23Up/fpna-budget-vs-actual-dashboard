"""
FP&A Budget vs Actual Variance Analysis

This script:
1. Loads monthly FP&A budget vs actual data.
2. Calculates revenue variance, cost variance, gross profit, operating profit, and margin KPIs.
3. Saves processed KPI output.
4. Generates charts for portfolio reporting.

Run from the project root:
    python src/fpna_analysis.py
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = PROJECT_ROOT / "data" / "raw" / "fpna_budget_actual_monthly.csv"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
IMAGE_DIR = PROJECT_ROOT / "images"


def calculate_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate FP&A KPI columns."""
    df = df.copy()

    df["Revenue_Variance"] = df["Revenue_Actual"] - df["Revenue_Budget"]
    df["Revenue_Variance_Pct"] = df["Revenue_Variance"] / df["Revenue_Budget"]

    df["Gross_Profit_Budget"] = df["Revenue_Budget"] - df["COGS_Budget"]
    df["Gross_Profit_Actual"] = df["Revenue_Actual"] - df["COGS_Actual"]

    df["Total_Opex_Budget"] = (
        df["Salaries_Budget"]
        + df["Marketing_Budget"]
        + df["Operations_Budget"]
        + df["Admin_Budget"]
    )

    df["Total_Opex_Actual"] = (
        df["Salaries_Actual"]
        + df["Marketing_Actual"]
        + df["Operations_Actual"]
        + df["Admin_Actual"]
    )

    df["Operating_Profit_Budget"] = df["Gross_Profit_Budget"] - df["Total_Opex_Budget"]
    df["Operating_Profit_Actual"] = df["Gross_Profit_Actual"] - df["Total_Opex_Actual"]
    df["Profit_Variance"] = df["Operating_Profit_Actual"] - df["Operating_Profit_Budget"]
    df["Operating_Margin_Actual"] = df["Operating_Profit_Actual"] / df["Revenue_Actual"]
    df["Revenue_Growth_Actual"] = df["Revenue_Actual"].pct_change()

    return df


def save_charts(df: pd.DataFrame) -> None:
    """Save portfolio charts."""
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(9, 5))
    plt.plot(df["Month_Name"], df["Revenue_Budget"] / 1000, marker="o", label="Budget Revenue")
    plt.plot(df["Month_Name"], df["Revenue_Actual"] / 1000, marker="o", label="Actual Revenue")
    plt.title("Revenue Budget vs Actual ($000)")
    plt.xlabel("Month")
    plt.ylabel("$000")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.savefig(IMAGE_DIR / "revenue_budget_vs_actual.png", dpi=150)
    plt.close()

    plt.figure(figsize=(9, 5))
    plt.bar(df["Month_Name"], df["Profit_Variance"] / 1000)
    plt.title("Operating Profit Variance by Month ($000)")
    plt.xlabel("Month")
    plt.ylabel("$000")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(IMAGE_DIR / "profit_variance_by_month.png", dpi=150)
    plt.close()

    expense_categories = ["Salaries", "Marketing", "Operations", "Admin"]
    actual_expenses = [
        df["Salaries_Actual"].sum() / 1000,
        df["Marketing_Actual"].sum() / 1000,
        df["Operations_Actual"].sum() / 1000,
        df["Admin_Actual"].sum() / 1000,
    ]

    plt.figure(figsize=(8, 5))
    plt.bar(expense_categories, actual_expenses)
    plt.title("Actual Opex by Category ($000)")
    plt.xlabel("Category")
    plt.ylabel("$000")
    plt.tight_layout()
    plt.savefig(IMAGE_DIR / "actual_opex_by_category.png", dpi=150)
    plt.close()


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(RAW_PATH)
    kpi_df = calculate_kpis(df)

    output_path = PROCESSED_DIR / "fpna_kpi_summary.csv"
    kpi_df.to_csv(output_path, index=False)

    save_charts(kpi_df)

    print("Analysis complete.")
    print(f"Processed file saved to: {output_path}")
    print(f"Charts saved to: {IMAGE_DIR}")


if __name__ == "__main__":
    main()
