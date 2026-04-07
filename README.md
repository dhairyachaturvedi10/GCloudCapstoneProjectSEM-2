# KU.SYS - Karnavati University Event Registration

## Project Overview
This is a modern, glassmorphic web application built as a Capstone Project to handle event registrations for Karnavati University. It features a responsive grid of 12 distinct events, a live global countdown timer, and an interactive registration portal.

![Version](https://img.shields.io/badge/version-1.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Ready-blue.svg)

**KU.SYS** is a full-stack, cloud-ready event registration platform built for Karnavati University's Tech Fest. It features a modern, cyberpunk-inspired glassmorphism UI, a secure Python/Flask backend, and an enterprise-grade PostgreSQL database designed to handle high-concurrency registration spikes.

---

## ✨ Key Features

* **Interactive Glassmorphism UI:** Built with raw CSS and Vanilla JavaScript, featuring neon gradient animations, custom scrollbars, and dynamic "pop-in" event modals.
* **Real-Time DOM Filtering:** A secure Admin Dashboard (`/admin`) that allows administrators to instantly search and filter student registrations in real-time without querying the database, reducing server load.
* **Live Countdown Engine:** A JavaScript-driven countdown timer synced to a master Python variable, ensuring all students see the exact time remaining until the festival.
* **Enterprise Security:** Utilizes parameterized SQL queries (`%s`) via `psycopg2` to completely eliminate the risk of SQL injection attacks during student registration.
* **Cloud-Ready Architecture:** Abstracted database connection logic, allowing for a seamless migration from a local environment to Google Cloud Run and Google Cloud SQL.

---

## 🛠️ Tech Stack

**Frontend (Client)**
* HTML5 & CSS3 (Custom animations, Flexbox, UI/UX)
* Vanilla JavaScript (ES6, Fetch API, DOM Manipulation)

**Backend (Server)**
* Python 3
* Flask (Routing, Server-Side Rendering, JSON API)

**Database**
* PostgreSQL (Relational DBMS)
* `psycopg2-binary` (Python Adapter)

---

## 💾 Database Schema

The application relies on the following PostgreSQL schema to guarantee data integrity:

```sql
CREATE TABLE registrations (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    college_id VARCHAR(50) NOT NULL,
    semester VARCHAR(20) NOT NULL,
    section VARCHAR(50) NOT NULL,
    event_name VARCHAR(100) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
---
##📖 KU.SYS: Complete Setup & Usage Guide
Welcome to the Karnavati University Event Registration Terminal (KU.SYS). This guide provides step-by-step instructions for evaluators, administrators, and future developers to set up the environment, run the server, and navigate the platform.

##PART 1: System Requirements & Setup
This section is for whoever is running the code for the first time.

1. Prerequisites
Before running the application, ensure your machine has the following software installed:

Python 3.8+ (Added to system PATH)

PostgreSQL (Version 14 or higher)

pgAdmin 4 (For database management)

Git (Optional, for downloading the repository)

2. Database Initialization
The application requires a PostgreSQL server to store student data securely.

Open pgAdmin 4 and log in with your master password.

In the left sidebar, right-click Databases ➔ Create ➔ Database.

Name the database exactly: ku_events and save.

Click on the new ku_events database, open the Query Tool (top menu), and execute the following SQL command to build the tables:

SQL
CREATE TABLE registrations (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    college_id VARCHAR(50) NOT NULL,
    semester VARCHAR(20) NOT NULL,
    section VARCHAR(50) NOT NULL,
    event_name VARCHAR(100) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
3. Application Configuration
Open the project folder in your code editor (e.g., VS Code).

Open the terminal and install the required Python libraries:

Bash
pip install -r requirements.txt
Open app.py. Locate the get_db_connection() function near the top of the file.

Important: Change the password="YOUR_ACTUAL_PASSWORD_HERE" to match the password you set when installing PostgreSQL.

4. Launching the Server
In your terminal, start the Flask web server by running:

Bash
python app.py
You should see a message indicating the server is running on http://127.0.0.1:5000. Leave this terminal open.

##PART 2: Using the Platform
This section explains how to navigate the two main interfaces of the application.

🖥️ The Student Experience (Frontend)
Access URL: http://localhost:5000

Viewing Events: When students arrive at the homepage, they will see a live countdown to Tech Fest and a grid of available events.

Interactive Modals: Clicking "View Details" on any event card triggers a glassmorphism popup containing the event description and a direct registration link.

Registration: * Clicking "Register" takes the user to the secure form.

The form features strict client-side validation (e.g., character limits on the Section field).

Upon successful submission, a secure background network request (Fetch API) saves the data, and a green success banner appears without refreshing the page.

🔐 The Administrator Experience (Backend)
Access URL: http://localhost:5000/admin

This hidden dashboard is designed for university staff to manage the influx of event registrations.

The Data Table: The dashboard automatically pulls a live feed of all registered students directly from the PostgreSQL database, sorting the newest registrations at the top.

Real-Time Search: Use the search bar at the top to type a student's Name, College ID, or Event Name. The table uses JavaScript to filter the results instantly, with zero server lag.

Record Deletion: If a student registers by mistake, click the neon-red DELETE button next to their name. A safety warning will appear. Confirming will permanently erase their record from the database and instantly refresh the table.

##PART 3: Codebase Architecture Map
For grading evaluators reviewing the codebase structure.

app.py: The core Flask server. Handles web routing, API endpoints, and direct communication with the PostgreSQL database.

schema.sql: Documentation file containing the exact SQL structure required for the database.

requirements.txt: Lists the external Python libraries needed (Flask and psycopg2-binary).

/templates/: Contains the HTML files (events.html, register.html, admin.html).

/static/: * style.css: Contains the global styling, CSS animations, and glassmorphism UI variables.

script.js: Handles frontend interactivity (modals, countdown timer, async form submissions).

admin.js: Powers the real-time search logic and delete API calls for the admin dashboard.
