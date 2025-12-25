import os
import json
import sqlite3

DB_NAME = "phonepe.db"
BASE_PATH = "pulse/data/aggregated/transaction/country/india/state"

if not os.path.exists(BASE_PATH):
    raise FileNotFoundError(f"Path not found: {BASE_PATH}")

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS aggregated_transaction (
    state TEXT,
    year INTEGER,
    quarter INTEGER,
    transaction_type TEXT,
    transaction_count INTEGER,
    transaction_amount REAL
)
""")

for state in os.listdir(BASE_PATH):
    state_path = os.path.join(BASE_PATH, state)
    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)
        for file in os.listdir(year_path):
            if file.endswith(".json"):
                quarter = int(file.split(".")[0])

                with open(os.path.join(year_path, file), "r", encoding="utf-8") as f:
                    data = json.load(f)

                for item in data["data"]["transactionData"]:
                    cursor.execute("""
                        INSERT INTO aggregated_transaction
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (
                        state.replace("-", " ").title(),
                        int(year),
                        quarter,
                        item["name"],
                        item["paymentInstruments"][0]["count"],
                        item["paymentInstruments"][0]["amount"]
                    ))

conn.commit()
conn.close()

print("✅ aggregated_transaction table created & data inserted")
