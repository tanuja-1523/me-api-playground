from fastapi import FastAPI, Query
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# ---------- Database Helpers ----------
def get_db():
    conn = sqlite3.connect("meapi.db")
    conn.row_factory = sqlite3.Row
    return conn

# ---------- Models ----------
class Profile(BaseModel):
    name: str
    email: str
    education: str = None
    github: str = None
    linkedin: str = None
    portfolio: str = None

class Project(BaseModel):
    title: str
    description: str
    link: str
    skill_id: int

# ---------- Routes ----------
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/profile")
def get_profile():
    conn = get_db()
    profile = conn.execute("SELECT * FROM profile LIMIT 1").fetchone()
    conn.close()
    return dict(profile) if profile else {}

@app.post("/profile")
def update_profile(p: Profile):
    conn = get_db()
    conn.execute("DELETE FROM profile")  # keep only 1 profile
    conn.execute(
        "INSERT INTO profile (name,email,education,github,linkedin,portfolio) VALUES (?,?,?,?,?,?)",
        (p.name, p.email, p.education, p.github, p.linkedin, p.portfolio),
    )
    conn.commit()
    conn.close()
    return {"message": "Profile updated"}

@app.get("/projects")
def get_projects(skill: str = Query(None)):
    conn = get_db()
    if skill:
        rows = conn.execute(
            "SELECT projects.* FROM projects JOIN skills ON projects.skill_id=skills.id WHERE skills.name=?",
            (skill,),
        ).fetchall()
    else:
        rows = conn.execute("SELECT * FROM projects").fetchall()
    conn.close()
    return [dict(r) for r in rows]

@app.get("/skills/top")
def get_top_skills():
    conn = get_db()
    rows = conn.execute("SELECT * FROM skills ORDER BY level DESC LIMIT 5").fetchall()
    conn.close()
    return [dict(r) for r in rows]

@app.get("/search")
def search(q: str):
    conn = get_db()
    rows = conn.execute(
        "SELECT 'project' as type, title as content FROM projects WHERE title LIKE ? OR description LIKE ? "
        "UNION ALL SELECT 'skill', name FROM skills WHERE name LIKE ? "
        "UNION ALL SELECT 'profile', name FROM profile WHERE name LIKE ? OR education LIKE ?",
        (f"%{q}%", f"%{q}%", f"%{q}%", f"%{q}%", f"%{q}%"),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]
