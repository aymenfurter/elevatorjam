from pydantic import BaseModel as PydanticBaseModel
from typing import List


class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class Song(BaseModel):
    file: List[str]
    name: str
    theme: str

class User(BaseModel):
    uid: str
    songs: List[str]

class State(BaseModel):
    users: List[User]
    


STATE = State(users=[])
