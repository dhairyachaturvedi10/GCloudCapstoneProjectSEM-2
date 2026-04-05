from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# ==========================================
# 🕒 MASTER TIMER SETTING 🕒
# Change this date/time, and it updates across the whole website!
# Format: YYYY-MM-DDTHH:MM:SS
FESTIVAL_DATE = "2026-04-10T08:00:00"
# ==========================================

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def events():
    # Pass the master date to the events page
    return render_template('events.html', target_date=FESTIVAL_DATE)

@app.route('/register')
def register_page():
    selected_event = request.args.get('event', '')
    # Pass the master date to the registration page
    return render_template('register.html', selected_event=selected_event, target_date=FESTIVAL_DATE)

@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()
    full_name = data.get('fullName')
    college_id = data.get('collegeId')
    semester = data.get('semester')
    section = data.get('section')
    event_name = data.get('eventName')

    # Security check for all fields
    if not all([full_name, college_id, semester, section, event_name]):
        return jsonify({"status": "error", "message": "SYSTEM ERROR: Missing Data Segments."}), 400

    conn = get_db_connection()
    conn.execute('''
        INSERT INTO registrations (full_name, college_id, semester, section, event_name) 
        VALUES (?, ?, ?, ?, ?)''', 
        (full_name, college_id, semester, section, event_name)
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": f"ACCESS GRANTED: Registered for {event_name}"})

if __name__ == '__main__':
    app.run(debug=True)