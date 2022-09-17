from fastapi import APIRouter
from backend.models.models import User
from backend.models.models import STATE

route = APIRouter()

@route.post("/user/{id}")
async def add_user(id: str, user: User) -> str:
    STATE.users.append(User)
    return "ok"