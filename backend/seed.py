import sqlite3

# Connect to database
conn = sqlite3.connect("meapi.db")
cursor = conn.cursor()

# Insert a profile
cursor.execute("""
INSERT INTO profile (name, email, education, github, linkedin, portfolio)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    "Tanuja Adlakha",
    "tanuja@example.com",
    "B.Tech Computer Science",
    "https://github.com/yourgithub",
    "https://linkedin.com/in/yourlinkedin",
    "https://yourportfolio.com"
))

# Insert skills
skills = [
    ("Python", 90),
    ("Machine Learning", 80),
    ("Data Visualization", 85)
]
cursor.executemany("INSERT INTO skills (name, level) VALUES (?, ?)", skills)

# Insert projects
projects = [
    ("Stock Price Prediction", "Predicted stock trends using LSTMs and sentiment analysis", "https://github.com/project1", 2),
    ("Interactive Dashboard", "Built a dashboard for visualizing data interactively", "https://github.com/project2", 3)
]
cursor.executemany("INSERT INTO projects (title, description, link, skill_id) VALUES (?, ?, ?, ?)", projects)

conn.commit()
conn.close()
print("✅ Database seeded with data!")
