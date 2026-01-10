from flask import Blueprint, request, jsonify, render_template
from analyze_url import analyze_reviews
from extensions import db
from models import SentimentResult

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    product_url = data.get("url")
    if not product_url:
        return jsonify({"error": "Missing URL"}), 400

    result = analyze_reviews(product_url)

    if not result["reviews"]:
        return jsonify({"error": "No reviews found"}), 404

    # Save only if reviews exist
    sentiment_record = SentimentResult(
        product_url=product_url,
        sentiment_text="Snapdeal Product",
        overall=result["overall"],
        avg_polarity=result["avg"],
        positive=result["summary"]["positive"],
        negative=result["summary"]["negative"],
        neutral=result["summary"]["neutral"]
    )
    db.session.add(sentiment_record)
    db.session.commit()

    return jsonify({
        "overall": result["overall"],
        "avg": result["avg"],
        "positive": result["summary"]["positive"],
        "negative": result["summary"]["negative"],
        "neutral": result["summary"]["neutral"]
    })

@routes.route("/history")
def history():
    results = SentimentResult.query.order_by(SentimentResult.created_at.desc()).all()
    return render_template("history.html", results=results)
