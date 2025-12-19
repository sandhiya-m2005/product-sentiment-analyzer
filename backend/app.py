from flask import Flask, request, jsonify
from flask_cors import CORS
from sentiment import analyze_sentiment

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    reviews = data.get("reviews", [])

    result = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for review in reviews:
        sentiment = analyze_sentiment(review)
        result[sentiment] += 1

    return jsonify({
        "dashboard": result,
        "total": len(reviews)
    })

if __name__ == "__main__":
    app.run(debug=True)