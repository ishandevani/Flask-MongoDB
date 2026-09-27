import os
from pymongo import MongoClient
from dotenv import load_dotenv
from app import app

# Load environment variables from .env
load_dotenv()

# Get MongoDB connection string
MONGO_URI = os.getenv("MONGO_URI")

# Create MongoDB client
client = MongoClient(MONGO_URI)

# Select database
db = client["flask_assignment"]

# Select collection
users_collection = db["users"]


def insert_user(name, age, email):
    """
    Insert user data into MongoDB Atlas.
    """

    user_data = {
        "name": name,
        "age": age,
        "email": email
    }

    result = users_collection.insert_one(user_data)

    return result.inserted_id

# Test insertion
# if __name__ == "__main__":
#     user_id = insert_user(
#         "Ishan",
#         24,
#         "ishan@example.com"
#     )

#     print("User inserted successfully!")
#     print("Inserted ID:", user_id)