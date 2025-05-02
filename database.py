import sqlite3

conn = sqlite3.connect('users-from-db.db')
cursor = conn.cursor()

# Table create karo (sirf 1 baar chalana h)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Users table created successfully!")
