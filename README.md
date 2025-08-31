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

API will be available at:http://127.0.0.1:5000

### 📂 Tech Stack
Python (Flask)
Render (Deployment)
JSON-based API
✨ Author

✨ Author

Terni Tanuja Adlakha
"github": ["https://github.com/tanuja-1523"],
    "linkedin": ["https://www.linkedin.com/in/terni-tanuja-adlakha-4a4a0925a/"]
