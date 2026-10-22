import sqlite3

conn = sqlite3.connect("database/leads.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM Leads")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()