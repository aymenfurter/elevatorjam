from fastapi import APIRouter
from backend.models.models import User
from backend.models.models import Elevator
from backend.models.models import STATE as state
import random
from typing import List
from rapidfuzz import process
from rapidfuzz import fuzz
from fastapi.responses import FileResponse


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
    song = random.sample(user.songs)
    song = await get_file(song)
    return song

async def get_file(filename: str):
    path = best_match(filename, list_files())
    return FileResponse(path=path)
    

def best_match(query: str, choices: List):
    print(choices)
    res = process.extract(query, choices, scorer=fuzz.WRatio, limit=1)
    print(res)
    return res

def list_files(path: str):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles