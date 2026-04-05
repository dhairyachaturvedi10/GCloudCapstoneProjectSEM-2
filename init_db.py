import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Drop the old table and create the new one
cursor.execute('DROP TABLE IF EXISTS registrations')

cursor.execute('''
    CREATE TABLE registrations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        college_id TEXT NOT NULL,
        semester TEXT NOT NULL,
        section TEXT NOT NULL,
        event_name TEXT NOT NULL
    )
''')

connection.commit()
connection.close()
print("Cyber-Bento Database initialized successfully!")