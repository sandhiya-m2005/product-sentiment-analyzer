

from textblob import TextBlob
from scraper import scrape_snapdeal_reviews

def analyze_reviews(product_url, max_reviews=50):
    reviews = scrape_snapdeal_reviews(product_url, max_reviews)
    if not reviews:
        return {
            "reviews": [],
            "sentiments": [],
            "summary": {"positive":0,"negative":0,"neutral":0},
            "avg": 0,
            "overall": "No Reviews"
        }

    summary = {"positive":0,"negative":0,"neutral":0}
    sentiments = []
    polarity_sum = 0

    for review in reviews:
        review = str(review or "")
        polarity = TextBlob(review).sentiment.polarity
        polarity_sum += polarity

        if polarity > 0:
            sentiments.append("Positive")
            summary["positive"] += 1
        elif polarity < 0:
            sentiments.append("Negative")
            summary["negative"] += 1
        else:
            sentiments.append("Neutral")
            summary["neutral"] += 1

    avg = round(polarity_sum / len(reviews), 2) if reviews else 0
    overall = "Neutral"
    if summary["positive"] > summary["negative"]:
        overall = "Positive"
    elif summary["negative"] > summary["positive"]:
        overall = "Negative"

    return {
        "reviews": reviews,
        "sentiments": sentiments,
        "summary": summary,
        "avg": avg,
        "overall": overall
    }
