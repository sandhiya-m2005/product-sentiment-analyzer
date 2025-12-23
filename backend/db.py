from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['sentiment_db']
products_collection = db['products']
reviews_collection = db['reviews']
