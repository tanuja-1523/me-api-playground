from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/profile")
def profile():
    return jsonify({
        "name": "Terni Tanuja Adlakha",
        "email": "adlakhatanuja15@gmail.com",
        "education": "B.Tech in Computer Science",
        "links": {
            "github": "https://github.com/tanuja-1523",
            "linkedin": "https://www.linkedin.com/in/terni-tanuja-adlakha-4a4a0925a/"
        }
    })

@app.route("/projects")
def projects():
    return jsonify([
        {
            "title": "Interactive Data Visualization Dashboard",
            "description": "Interactive data visualization dashboard project",
            "link": "https://github.com/tanuja-1523/interactive-data-visualization-dashboard",
            "skills": ["Python", "Data Visualization", "Dashboard"]
        },
        {
            "title": "Stock Price Prediction with Sentiment Analysis (LSTM)",
            "description": "ML project using sentiment analysis + LSTM for stock price prediction",
            "link": "https://github.com/tanuja-1523/Stock-Price-Prediction-with-Sentiment-Analysis-LSTM",
            "skills": ["Python", "ML", "LSTM", "Sentiment Analysis"]
        },
        {
            "title": "Twitter Hate Speech Classifier",
            "description": "NLP project for detecting hate speech in tweets",
            "link": "https://github.com/tanuja-1523/twitter-hate-speech-classifier",
            "skills": ["Python", "NLP", "Text Classification"]
        }
    ])

@app.route("/skills/top")
def skills():
    return jsonify(["Python", "Flask", "Big Data", "Machine Learning", "NLP", "Deep Learning"])

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)
