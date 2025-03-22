from serializers import user as serializer
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from schemas.user import UserCreate
from database import user_collection
from datetime import datetime


class UserCrud:

    @staticmethod
    def create_user(user_data: UserCreate):
        user_data = jsonable_encoder(user_data)
        user_data["created_at"] = datetime.now()
        user_document_data = user_collection.insert_one(user_data)
        user_id = user_document_data.inserted_id
        user = user_collection.find_one({"_id": ObjectId(user_id)})
        return serializer.user_serializer(user)
    
    
    @staticmethod
    def get_user(user_id: str):
       if not ObjectId.is_valid(user_id):
            return {"error": "Invalid ObjectId format"}
       user = user_collection.find_one({"_id": ObjectId(user_id)})
       return serializer.user_serializer(user)
    
    @staticmethod
    def list_users():
        users = user_collection.find()
        return serializer.users_serializer(list(users))

    @staticmethod
    def delete_user(user_id: str):
        if not ObjectId.is_valid(user_id):
            return {"error": "Invalid ObjectId format"}
        delete = user_collection.delete_one({"_id": ObjectId(user_id)})
        if not delete:
            return {"error": "user not found"}
        return {"deleted_count": delete.deleted_count}


user_crud = UserCrud()
