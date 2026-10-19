from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CSV_FILE = ROOT / "data" / "cleaned_retail.csv"
DB_FILE = ROOT / "data" / "retail.db"

print("Loading cleaned data into SQLite...")

df = pd.read_csv(CSV_FILE)

with sqlite3.connect(DB_FILE) as conn:
    df.to_sql(
        "retail",
        conn,
        if_exists="replace",
        index=False,
        chunksize=10000
    )

    count = pd.read_sql_query(
        "SELECT COUNT(*) AS total_rows FROM retail",
        conn
    )
    print(f"Rows loaded: {count.iloc[0, 0]:,}")

print(f"Database created: {DB_FILE}")
