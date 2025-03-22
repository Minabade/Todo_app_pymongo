def todo_serializer(todo_document) -> dict:
    return {
        "id": str(todo_document.get("_id")),
        "user_id": str(todo_document.get("user_id")),
        "title": todo_document.get("title"),
        "description": todo_document.get("description"),
        "is_completed": todo_document.get("is_completed")
    }


def todos_serializer(todo_documents) -> list:
    return [todo_serializer(todo_document) for todo_document in todo_documents]

