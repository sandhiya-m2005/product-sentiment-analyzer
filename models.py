from extensions import db
from datetime import datetime

class SentimentResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_url = db.Column(db.String(300), nullable=False)  # Make sure this exists
    sentiment_text = db.Column(db.String(200), nullable=False)
    overall = db.Column(db.String(50))
    avg_polarity = db.Column(db.Float)
    positive = db.Column(db.Integer)
    negative = db.Column(db.Integer)
    neutral = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
