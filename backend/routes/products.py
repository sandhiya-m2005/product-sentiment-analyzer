from flask import Blueprint, request, jsonify
from scraper import scrape_reviews
from sentiment import analyze_sentiment
from db import reviews_collection

product_routes = Blueprint('products', __name__)

@product_routes.route('/analyze', methods=['POST'])
def analyze_product():
    data = request.json
    url = data.get('url')

    reviews = scrape_reviews(url)
    results = []

    for review in reviews:
        sentiment = analyze_sentiment(review)
        results.append({
            'review': review,
            'sentiment': sentiment
        })
        reviews_collection.insert_one({
            'review': review,
            'sentiment': sentiment
        })

    return jsonify(results)