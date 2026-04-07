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
