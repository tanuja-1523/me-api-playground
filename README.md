# 🌐 Me-API Playground

A simple personal API that serves profile, skills, and projects in JSON format.  
Deployed and accessible online 🚀

---

## 🔗 Live API
[👉 Check Live Deployment](https://me-api-playground-4-pdv6.onrender.com)

---

## 📄 Resume
[👉 View Resume](https://drive.google.com/file/d/1mQ1DMEJ32JcOsYRlmd2_TH0zh6geMuGZ/view?usp=drive_link)

---

## 📌 Available Endpoints

### 1. Health Check
GET /health

**Response**
json
{
  "status": "ok"
}

### 2. Profile
GET /profile


Response

{
  "name": "Tanuja Adlakha",
  "email": "adlakhatanuja15@gmail.com",
  Education: B.Tech in Computer Science
  "links": {
    "github": ["https://github.com/tanuja-1523"],
    "linkedin": ["https://www.linkedin.com/in/terni-tanuja-adlakha-4a4a0925a/"]
  }
}
### 3. Projects
GET /projects


Response
1. "title": Interactive Data Visualization Dashboard
"description": Interactive data visualization dashboard project

"Project Link"- ["https://github.com/tanuja-1523/interactive-data-visualization-dashboard"]

"skills"- Python, Data Visualization, Dashboard

2. "title": Stock Price Prediction with Sentiment Analysis (LSTM)
"description": ML project using sentiment analysis + LSTM for stock price prediction

"Project Link"- ["https://github.com/tanuja-1523/Stock-Price-Prediction-with-Sentiment-Analysis-LSTM"]

"skills"- Python ML LSTM Sentiment Analysis

3. "title": Twitter Hate Speech Classifier
"description": NLP project for detecting hate speech in tweets

"Project Link"-["https://github.com/tanuja-1523/twitter-hate-speech-classifier']

"skills"- Python NLP Text Classification

### 4.Top Skills
GET /skills/top


Response

["Python", "Machine Learning", "NLP"]

### 🚀 Local Development

Clone the repo and run locally:

git clone https://github.com/tanuja-1523/me-api-playground.git
cd me-api-playground
pip install -r requirements.txt
python app.py

API will be available at: ["https://me-api-playground-4-pdv6.onrender.com"]

### 📂 Tech Stack
Python (Flask)
Render (Deployment)
JSON-based API

###  Screenshots 
<img width="1731" height="830" alt="Screenshot 2025-09-01 013306" src="https://github.com/user-attachments/assets/eb1d81a0-fe8a-458a-b797-e9bc9e71e945" />
 <img width="1887" height="829" alt="Screenshot 2025-08-30 193239" src="https://github.com/user-attachments/assets/950e096a-194f-4c13-87e4-bf2577e0b82e" />
<img width="1796" height="836" alt="Screenshot 2025-09-01 154342" src="https://github.com/user-attachments/assets/c0f45f92-f3b5-4a33-9db1-24fbdb1d512f" />
<img width="1103" height="527" alt="Screenshot 2025-09-01 154349" src="https://github.com/user-attachments/assets/342477e8-cefb-44c7-aab9-c5dd072f0e9e" />


### Clear Schema (Track A)

Entity / Resource	Fields / Attributes	Description	Notes / Indexing
users	id, name, email	Stores all user details	Indexed by id for fast lookup
projects	id, title, ownerId, status	Stores project information	Indexed by id and ownerId
tasks	id, projectId, title, status	Tasks under each project	Indexed by projectId for efficient querying

Notes:

All IDs are unique and auto-generated.

Relationships are maintained via ownerId and projectId.

Designed for efficient read-heavy operations.

### Remarks

# Limits / Trade-offs:

The current implementation uses a JSON/mock database, which is not suitable for large-scale production data.

Read operations are optimized via indexing, but write-heavy operations may experience slower performance.

No authentication/authorization is implemented yet.

# Next Steps / Improvements:

Migrate to a real database like MongoDB or PostgreSQL.

Add authentication and role-based access control.

Implement caching and pagination for large datasets.

Add unit tests and error handling for robustness.

✨ Author

Terni Tanuja Adlakha
"github": ["https://github.com/tanuja-1523"],
    "linkedin": ["https://www.linkedin.com/in/terni-tanuja-adlakha-4a4a0925a/"]
