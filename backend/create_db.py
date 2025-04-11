import sqlite3
import pandas as pd

# Load Excel file (Update path if necessary)
excel_file = "backend/upload/fs.xml.xlsx"

# Connect to SQLite database
conn = sqlite3.connect("backend/database.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usn TEXT UNIQUE,
    name TEXT,
    project_title TEXT,
    guide TEXT
)
""")

# Read data from Excel
df = pd.read_excel(excel_file, dtype=str)  # Ensure all data is read as strings

# 🔥 Ensure Correct Column Mapping
expected_columns = ["USN", "Name", "Project Title", "Guide"]
df.columns = df.columns.str.strip()  # Remove any extra spaces in column names
df = df[expected_columns]  # Select only required columns, in correct order

# Insert data into database
for _, row in df.iterrows():
    cursor.execute(
        "INSERT OR IGNORE INTO students (usn, name, project_title, guide) VALUES (?, ?, ?, ?)",
        (row["USN"], row["Name"], row["Project Title"], row["Guide"])
    )

# Commit and close
conn.commit()
conn.close()

print("✅ Database Created & Data Inserted Successfully!")
