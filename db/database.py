from pymongo import MongoClient
import os
from dotenv import load_dotenv

MONGODB_URI = os.getenv("MONGODB_URL")  # For local MongoDB
client = MongoClient(MONGODB_URI)
db = client["test_database"]  # Use a database named "test_database"
users_collection = db["users"]  # Use a collection named "users"