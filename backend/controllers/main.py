from fastapi import APIRouter
from backend.models.models import User
from backend.models.models import Elevator
from backend.models.models import STATE as state
import random


route = APIRouter()

@route.post("/user")
async def add_user(userId: str, music: str) -> str:
    if userId in list(user.uid for user in state.users):
        next(map(lambda x: x.songs.append(music) , [user for user in state.users if user.uid == userId]))
    else:
        state.users.append(User(uid=userId, songs =[music]))
    print(state.users)
    return "ok"

@route.post("/enter")
async def enters(userId: str, elevatorId: str):
    if elevatorId in list(elevator for elevator in state.elevators):
        next(map(lambda x: x.users.append(userId) , [elevator for elevator in state.elevators if elevator.elevatorId == elevatorId]))
    else:
        state.elevators.append(Elevator(elevatorId=elevatorId, users=[userId]))
    print(state.elevators)
    
@route.get("/song/")
async def get_song_for(elevatorId: str):
    elevator = [elevator for elevator in state.elevators if elevator.elevatorId == elevatorId].pop(0)
    userId = elevator.users.pop(0)
    user = [user for user in state.users if user.uid == userId].pop(0)
    try:
        song = random.sample(user.songs, k=1)
    except:
        song = random.sample(["rock", "pop", "hiphop", "k-pop"])
    return song
