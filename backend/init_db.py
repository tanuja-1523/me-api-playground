import sqlite3

# Connect (creates meapi.db if it doesn’t exist)
conn = sqlite3.connect("meapi.db")
cursor = conn.cursor()

# Create tables
cursor.executescript("""
CREATE TABLE IF NOT EXISTS profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    education TEXT,
    github TEXT,
    linkedin TEXT,
    portfolio TEXT
);

CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    level INTEGER
);

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    link TEXT,
    skill_id INTEGER,
    FOREIGN KEY (skill_id) REFERENCES skills(id)
);
""")

conn.commit()
conn.close()
print("Database initialized ✅")
