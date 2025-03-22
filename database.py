import os
from pymongo import mongo_client
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_CONNECTION_URI = os.environ.get('MONGO_DB_CONNECTION_URI')

client = mongo_client.MongoClient(MONGO_DB_CONNECTION_URI)

user_collection = client["todoapp"]["users"]
todo_collection = client["todoapp"]["todo"]
