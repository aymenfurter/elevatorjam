from fastapi import APIRouter
from backend.models.models import User
from backend.models.models import Elevator
from backend.models.models import STATE as state
import random
import copy

route = APIRouter()


@route.post("/user")
async def add_user(userId: str, music: str) -> str:
    
    def change_song(user: User):
        user.songs = [music]
    
    if userId in list(user.uid for user in state.users):
        next(map(change_song, [user for user in state.users if user.uid == userId]))
    else:
        state.users.append(User(uid=userId, songs =[music]))
    print(state.users)
    return "ok"

@route.post("/enter")
async def enters(userId: str, elevatorId: str):
    if elevatorId in list(elevator.elevatorId for elevator in state.elevators):
        next(map(lambda x: x.users.append(userId) , [elevator for elevator in state.elevators if elevator.elevatorId == elevatorId]))
    else:
        state.elevators.append(Elevator(elevatorId=elevatorId, users=[userId]))
    print(state.elevators)
    
@route.get("/song/")
async def get_song_for(elevatorId: str):
    try:
        elevator = [elevator for elevator in state.elevators if elevator.elevatorId == elevatorId][0]
        userId = elevator.users[0]
        user = copy.deepcopy([user for user in state.users if user.uid == userId][0])
        song = random.sample(user.songs, k=1)
    except Exception as e:
        print(e)
        song = random.sample(["rock", "pop"], k=1)
    return song

@route.get("/ping")
async def ping():
    return "pong"