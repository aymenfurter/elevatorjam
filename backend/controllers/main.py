from fastapi import APIRouter
from backend.models.models import User
from backend.models.models import STATE

route = APIRouter()

@route.post("/user")
async def add_user(userId: str, music: str) -> str:
    if userId in list(user.uid for user in STATE.users):
        next(map(lambda x: x.songs.append(music) , [user for user in STATE.users if user.uid == userId]))
    else:
        STATE.users.append(User(uid=userId, songs =[music]))
    print(STATE.users)
    return "ok"

@route.post("/enter")
async def enters(userId: str, elevatorId: str):
    pass