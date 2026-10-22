import sqlite3
import pandas as pd

conn = sqlite3.connect("database/leads.db")

df = pd.read_sql(

    "SELECT * FROM LEADS",
    conn
)

df.to_excel(
    "leads_report.xlsx",
    index = False
)

conn.close()

print("Export Complete")

