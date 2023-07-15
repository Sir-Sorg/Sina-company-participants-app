from pymongo import MongoClient
from dotenv import dotenv_values

# Load MongoDb uri link from environment variables
secrets = dotenv_values(".env")
client = MongoClient(secrets['uri'])

db = client["twitter_data"]
collection = db["twitter_collection"]
