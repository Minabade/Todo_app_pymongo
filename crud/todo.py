from serializers import todo as serializer
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from schemas.todo import TodoCreate
from database import todo_collection



class TodoCrud:

    @staticmethod
    def create_todo(todo_data: TodoCreate):
        todo_data = jsonable_encoder(todo_data)
        todo_document_data = todo_collection.insert_one(todo_data)
        todo_id = todo_document_data.inserted_id
        todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
        return serializer.todo_serializer(todo)
    
    @staticmethod
    def get_todo(todo_id: str):
        if not ObjectId.is_valid(todo_id):
            return {"error": "Invalid ObjectId format"}
        todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
        return serializer.todo_serializer(todo)

    @staticmethod
    def list_todos():
        todos = todo_collection.find()
        return serializer.todos_serializer(list(todos))

    @staticmethod
    def update_todo(todo_id: str, todo_data: TodoCreate):
        if not ObjectId.is_valid(todo_id):
            return {"error": "Invalid ObjectId format"}
        new_data = jsonable_encoder(todo_data)
        update = todo_collection.update_one({"_id":ObjectId(todo_id)}, {"$set": new_data})
        return {"matched_count": update.matched_count, "modified_count": update.modified_count}


    @staticmethod
    def delete_todo(todo_id: str):
        try:
            obj_id = ObjectId(todo_id)  
        except Exception:
            return {"error": "Invalid ObjectId format"}
        
        todo = todo_collection.find_one({"_id": obj_id})
        
        if not todo:
            return {"error": "Todo not found"}
        
        delete = todo_collection.delete_one({"_id": obj_id})  
        return {"deleted_count": delete.deleted_count}

    

    @staticmethod
    def list_todos_by_user(user_id: str):
        if not ObjectId.is_valid(user_id):
            return {"error": "Invalid ObjectId format"}
        user_todos =  todo_collection.find({"user_id": user_id})
        user_todos_all = list(user_todos)  

        print(f"Found todos: {user_todos_all}") 
    
        if not user_todos_all:
            return []  
        return serializer.todos_serializer(user_todos_all)
       


todo_crud = TodoCrud()
