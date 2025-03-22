def user_serializer(user_document) -> dict:
    return {
        "id": str(user_document.get("_id")),
        "username": user_document.get("username"),
        "created_at": str(user_document.get("created_at"))
    }


def users_serializer(users_documents) -> list:
    user_schemas = []
    for user_document in users_documents:
        user_schemas.append(user_serializer(user_document))
    return user_schemas
