import json
import sqlite3


with open('clean.json', 'r') as f:
    data = json.load(f)


conn = sqlite3.connect("pipeline.db")

conn.execute("CREATE TABLE IF NOT EXISTS clean_appointments (id INTEGER, provider TEXT, status TEXT, minutes INTEGER)")
conn.execute("DELETE FROM clean_appointments")
for row in data:
    conn.execute("INSERT INTO clean_appointments VALUES (?, ?, ?, ?)", (int(row['id']), row['provider'], row['status'], row['minutes']))

conn.commit()