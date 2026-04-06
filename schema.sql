-- Karnavati University Event Registration Schema
-- Deployed on PostgreSQL

CREATE TABLE registrations (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    college_id VARCHAR(50) NOT NULL,
    semester VARCHAR(20) NOT NULL,
    section VARCHAR(50) NOT NULL,
    event_name VARCHAR(100) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);