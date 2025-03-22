from fastapi import FastAPI
from routers import todo, user

app = FastAPI()

app.include_router(user.router)
app.include_router(todo.router)


@app.get("/")
def home():
    return {"message": "Welcome to todoapp"}
