from fastapi import APIRouter
from backend.models.models import User
from backend.models.models import STATE

route = APIRouter()

@route.post("/user/{id}/{song}")
async def add_user(id: str, song: str) -> str:
    if id in list(user.uid for user in STATE.users):
        next(map(lambda x: x.songs.append(song) , [user for user in STATE.users if user.uid == id]))
    else:
        STATE.users.append(User(uid=id, songs =[song]))
    print(STATE.users)
    return "ok"