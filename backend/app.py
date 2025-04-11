from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, template_folder="templates")  # Ensure correct template path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    usn = request.form['usn'].strip()
    print(f"🔍 Searching for USN: {usn}")  # Debugging

    # Connect to database
    conn = sqlite3.connect("backend/database.db")  # Ensure correct path
    cursor = conn.cursor()

    # Fetch student details
    cursor.execute("SELECT usn, name, project_title, guide FROM students WHERE usn = ?", (usn,))
    student = cursor.fetchone()
    
    conn.close()

    if student:
        print(f"✅ Found: {student}")  # Debugging
    else:
        print("❌ No student found.")  # Debugging

    return render_template('results.html', student=student, usn=usn)

