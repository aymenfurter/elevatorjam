import asyncio
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path
from backend.controllers.main import route

app = FastAPI(version="1.0.0", title="server")
app.include_router(router=route)


@app.get("/", response_class=HTMLResponse)
async def home() -> str:
    html = Path("frontend/app/index.html").read_text()
    return html


app.mount("/", StaticFiles(directory="frontend/app"), name="frontend")


@app.on_event("startup")
async def on_startup():
    print("startup")
