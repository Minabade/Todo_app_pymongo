from pydantic import BaseModel


class TodoBase(BaseModel):
    user_id: str
    title: str
    description: str
    is_completed: bool = False


class Todo(TodoBase):
    id: str


class TodoCreate(TodoBase):
    pass
