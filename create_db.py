import sqlite3

conn = sqlite3.connect("database/leads.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Leads (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Phone TEXT NOT NULL,
    Email TEXT NOT NULL,
    CreatedAt TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database created successfully.")
