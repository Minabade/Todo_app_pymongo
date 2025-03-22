from fastapi import APIRouter, HTTPException
from crud.user import user_crud
from schemas import user as user_schema

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user_endpoint(user: user_schema.UserCreate):
    return user_crud.create_user(user)

@router.get("/{user_id}", response_model=user_schema.User)
def get_user_endpoint(user_id: str):
    user = user_crud.get_user(user_id)
    if "error" in user:
        raise HTTPException(status_code=400, detail=user["error"])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user["created_at"] = user["created_at"].isoformat()
    return user


@router.get("/", response_model=list[user_schema.User])
def list_users_endpoint():
    return user_crud.list_users()





@router.delete("/{user_id}")
def delete_user_endpoint(user_id: str):
    deleted = user_crud.delete_user(user_id)
    if "error" in deleted:
        if deleted["error"] == "Invalid ObjectId format":
            raise HTTPException(status_code=400, detail=deleted["error"])  
        raise HTTPException(status_code=404, detail=deleted["error"]) 
       
    if deleted["deleted_count"] == 0:
        raise HTTPException(status_code=404, detail="User was not found or already deleted")
    return {"message": "User deleted successfully"}





