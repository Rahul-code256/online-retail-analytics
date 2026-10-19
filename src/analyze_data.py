from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "cleaned_retail.csv"
REPORTS = ROOT / "reports"
CHARTS = REPORTS / "charts"

CHARTS.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["InvoiceDate"])

# Key business metrics
total_revenue = df["Revenue"].sum()
total_orders = df["InvoiceNo"].nunique()
total_customers = df["CustomerID"].nunique()
total_products = df["StockCode"].nunique()
total_countries = df["Country"].nunique()
total_units = df["Quantity"].sum()

print("\n========== RETAIL BUSINESS SUMMARY ==========")
print(f"Total revenue:       {total_revenue:,.2f}")
print(f"Unique orders:       {total_orders:,}")
print(f"Unique customers:    {total_customers:,}")
print(f"Unique products:     {total_products:,}")
print(f"Countries served:    {total_countries:,}")
print(f"Units sold:          {total_units:,}")

# 1. Top 10 products by revenue
top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products.to_csv(REPORTS / "top_products.csv")
top_products.sort_values().plot(kind="barh", figsize=(10, 6))
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.tight_layout()
plt.savefig(CHARTS / "top_products.png", dpi=150)
plt.close()

# 2. Top 10 countries by revenue
top_countries = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_countries.to_csv(REPORTS / "top_countries.csv")
top_countries.sort_values().plot(kind="barh", figsize=(10, 6))
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue")
plt.tight_layout()
plt.savefig(CHARTS / "top_countries.png", dpi=150)
plt.close()

# 3. Monthly revenue trend
df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)
monthly_revenue = df.groupby("Month")["Revenue"].sum()

monthly_revenue.to_csv(REPORTS / "monthly_revenue.csv")
monthly_revenue.plot(figsize=(12, 5), marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(CHARTS / "monthly_revenue.png", dpi=150)
plt.close()

# 4. Top products by quantity sold
top_quantity = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
top_quantity.to_csv(REPORTS / "top_quantity_products.csv")

print("\nAnalysis completed successfully.")
print(f"Reports saved in: {REPORTS}")
print(f"Charts saved in:  {CHARTS}")
print("\nTop 5 products by revenue:")
print(top_products.head().to_string())
print("\nTop 5 countries by revenue:")
print(top_countries.head().to_string())
print("\nMonthly revenue:")
print(monthly_revenue.to_string())
