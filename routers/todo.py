from fastapi import APIRouter, HTTPException
from crud.todo import todo_crud
from schemas import todo as todo_schema

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("/", response_model=todo_schema.Todo)
def create_todo_endpoint(todo: todo_schema.TodoCreate):
    return todo_crud.create_todo(todo)

@router.get("/{todo_id}", response_model=todo_schema.Todo)
def get_todo_endpoint(todo_id: str):
    todo = todo_crud.get_todo(todo_id)
    if "error" in todo:
        raise HTTPException(status_code=400, detail=todo["error"])
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.get("/", response_model=list[todo_schema.Todo])
def list_todos_endpoint():
    return todo_crud.list_todos()


@router.put("/{todo_id}")
def update_todo_endpoint(
    todo_id: str, todo: todo_schema.TodoCreate):
    updated_todo = todo_crud.update_todo(todo_id, todo)
    if "error" in updated_todo:
        raise HTTPException(status_code=400, detail=updated_todo["error"])
    if updated_todo["matched_count"] == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    if updated_todo["modified_count"] == 0:
        return {"message": "No changes made to the todo"}
    return {"message": "Todo updated successfully"}


@router.delete("/{todo_id}")
def delete_todo_endpoint(todo_id: str):
    deleted = todo_crud.delete_todo(todo_id)
    if "error" in deleted:
        if deleted["error"] == "Invalid ObjectId format":
            raise HTTPException(status_code=400, detail=deleted["error"])  
        raise HTTPException(status_code=404, detail=deleted["error"]) 
       
    if deleted["deleted_count"] == 0:
        raise HTTPException(status_code=404, detail="Todo was not found or already deleted")
    return {"message": "Todo deleted successfully"}


@router.get("/user/{user_id}", response_model=list[todo_schema.Todo])
def get_todos_for_user(user_id: str):
    todos = todo_crud.list_todos_by_user(user_id)
    if "error" in todos:
        raise HTTPException(status_code=400, detail=todos["error"])
    if not todos:
        raise HTTPException(status_code=404, detail="No todos found for this user")
    return todos


