from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(CORSMiddleware, allow_origins=origins)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sudoku")
def get_sudoku():
    grid = [
        [None, None, None, None, None, None, None, None, None, None, None],
        [None, None, 1, None, None, 5, None, None, None, None, None],
        [None, 3, None, None, None, None, 7, 2, None, 6, None],
        [None, None, None, None, None, 1, 6, None, None, 7, None],
        [None, 4, None, None, None, 6, None, None, None, None, None],
        [None, None, None, None, None, None, 3, 9, None, 5, None],
        [None, None, 3, 9, None, None, 1, None, 2, None, None],
        [None, 8, None, 4, None, None, None, None, 6, None, None],
        [None, None, 7, None, None, None, None, None, None, None, None],
        [None, 6, None, None, None, None, None, None, 5, 9, None],
        [None, None, None, None, None, None, None, None, None, None, None],
    ]

    return {
        "grid": grid,
        "variants": {},
        "ws_path": "/ws",
    }


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
