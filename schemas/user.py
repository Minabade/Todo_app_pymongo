from datetime import datetime
from pydantic import BaseModel
from typing import Union


class UserBase(BaseModel):
    username: str


class User(BaseModel):
    id: str
    created_at: Union[datetime, str] = datetime.now()
    class Config:
       
        json_encoders = {
            datetime: lambda v: v.isoformat()  
        }


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
