
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parent.parent
DB_FILE = ROOT / "data" / "retail.db"

queries = {
    "Total revenue": """
        SELECT ROUND(SUM(Revenue), 2)
        FROM retail
    """,
    "Top 5 countries": """
        SELECT Country, ROUND(SUM(Revenue), 2) AS revenue
        FROM retail
        GROUP BY Country
        ORDER BY revenue DESC
        LIMIT 5
    """,
    "Average order value": """
        SELECT ROUND(SUM(Revenue) /
        COUNT(DISTINCT InvoiceNo), 2)
        FROM retail
    """
}

with sqlite3.connect(DB_FILE) as conn:
    for title, query in queries.items():
        print(f"\n--- {title} ---")
        for row in conn.execute(query):
            print(row)
