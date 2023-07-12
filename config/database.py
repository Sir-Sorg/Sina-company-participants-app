from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4uzsusr.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

db = client["twitter_data"]
collection = db["twitter_collection"]
