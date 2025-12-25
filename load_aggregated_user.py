import os
import json
import sqlite3

DB_NAME = "phonepe.db"
BASE_PATH = "pulse/data/aggregated/user/country/india/state"

if not os.path.exists(BASE_PATH):
    raise FileNotFoundError(f"Path not found: {BASE_PATH}")

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS aggregated_user (
    state TEXT,
    year INTEGER,
    quarter INTEGER,
    registered_users INTEGER,
    app_opens INTEGER
)
""")

# Load data
for state in os.listdir(BASE_PATH):
    state_path = os.path.join(BASE_PATH, state)
    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)
        for file in os.listdir(year_path):
            if file.endswith(".json"):
                quarter = int(file.split(".")[0])

                with open(os.path.join(year_path, file), "r", encoding="utf-8") as f:
                    data = json.load(f)

                users = data["data"]["aggregated"]["registeredUsers"]
                opens = data["data"]["aggregated"]["appOpens"]

                cursor.execute("""
                    INSERT INTO aggregated_user
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    state.replace("-", " ").title(),
                    int(year),
                    quarter,
                    users,
                    opens
                ))

conn.commit()
conn.close()

print("✅ aggregated_user table created & data inserted")
