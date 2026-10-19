from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = ROOT / "data" / "Online Retail.xlsx"
OUTPUT_FILE = ROOT / "data" / "cleaned_retail.csv"

def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {INPUT_FILE}")

    print("Loading retail dataset...")
    df = pd.read_excel(INPUT_FILE)

    print(f"Original rows: {len(df):,}")
    print(f"Original columns: {list(df.columns)}")

    # Standardize column names
    df.columns = df.columns.str.strip()

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove rows missing essential fields
    required = ["InvoiceNo", "StockCode", "Quantity", "InvoiceDate",
                "UnitPrice", "CustomerID", "Country"]
    existing_required = [c for c in required if c in df.columns]
    df = df.dropna(subset=existing_required)

    # Remove cancelled invoices and invalid transactions
    df["InvoiceNo"] = df["InvoiceNo"].astype(str)
    df = df[~df["InvoiceNo"].str.startswith("C")]
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

    # Create a revenue column
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    # Save cleaned data
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

    print(f"Cleaned rows: {len(df):,}")
    print(f"Rows removed: {len(pd.read_excel(INPUT_FILE)) - len(df):,}")
    print(f"Saved cleaned dataset to: {OUTPUT_FILE}")
    print("\nPreview:")
    print(df.head().to_string(index=False))

if __name__ == "__main__":
    main()
