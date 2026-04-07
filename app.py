from flask import Flask, render_template, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Master Variable for the Global Countdown Timer
FESTIVAL_DATE = "2026-04-10T23:59:00"

# Database Connection Helper (PostgreSQL)
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="ku_events",
        user="postgres",
        password="Dhiru9"  # Change this to your pgAdmin password
    )
    return conn

# 1. The Event Directory Page (Home)
@app.route('/')
def events():
    return render_template('events.html', target_date=FESTIVAL_DATE)

# 2. The Registration Terminal Page
@app.route('/register')
def register_page():
    # This grabs the specific event from the URL if the user clicked "Register Now"
    selected_event = request.args.get('event', '')
    return render_template('register.html', target_date=FESTIVAL_DATE, selected_event=selected_event)

# 3. The Secure API Endpoint for Form Submissions
@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()
    
    full_name = data.get('fullName')
    college_id = data.get('collegeId')
    semester = data.get('semester')
    section = data.get('section')
    event_name = data.get('eventName')

    # Basic Server-Side Security/Validation
    if not all([full_name, college_id, semester, section, event_name]):
        return jsonify({"status": "error", "message": "Missing required fields"}), 400

    try:
        # Open the secure tunnel to PostgreSQL
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Safely insert the data using %s to prevent SQL Injection
        cur.execute('''
            INSERT INTO registrations (full_name, college_id, semester, section, event_name) 
            VALUES (%s, %s, %s, %s, %s)''', 
            (full_name, college_id, semester, section, event_name)
        )
        
        # Save the transaction and close the tunnel
        conn.commit()
        cur.close()
        conn.close()
        
        # Send the success signal back to JavaScript
        return jsonify({"status": "success", "message": "ACCESS GRANTED: PROTOCOL SECURED."})
        
    except Exception as e:
        # If the database fails (e.g., wrong password), print the error to the terminal and notify the frontend
        print(f"Database Error: {e}")
        return jsonify({"status": "error", "message": "Database connection failed"}), 500

# --- ADMIN PANEL ROUTES ---

# 1. Serve the Admin HTML Page
@app.route('/admin')
def admin_page():
    return render_template('admin.html')

# 2. API to Fetch All Registrations
@app.route('/api/registrations', methods=['GET'])
def get_registrations():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Fetch everything, newest first
        cur.execute("SELECT id, full_name, college_id, event_name FROM registrations ORDER BY id DESC")
        rows = cur.fetchall()
        
        # Format the SQL data into a list of Python dictionaries
        registration_list = []
        for row in rows:
            registration_list.append({
                "id": row[0],
                "fullName": row[1],
                "collegeId": row[2],
                "eventName": row[3]
            })
            
        cur.close()
        conn.close()
        return jsonify(registration_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 3. API to Delete a Registration
@app.route('/api/registrations/<int:reg_id>', methods=['DELETE'])
def delete_registration(reg_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Delete the specific row using the ID passed in the URL
        cur.execute("DELETE FROM registrations WHERE id = %s", (reg_id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask Server
if __name__ == '__main__':
    app.run(debug=True)