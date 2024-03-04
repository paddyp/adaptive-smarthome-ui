from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
import utils.utils as utils
from utils.const import get_internal_server_error
import json
import logging

from sql_app.database import SessionLocal
from sql_app import crud
from utils.const import get_broadcast_data_dict

import debugpy
debugpy.listen(("0.0.0.0", 3000))

app = FastAPI()
logger = logging.getLogger(__name__)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user/")
async def create_user(db: Session = Depends(get_db)):
    # crud.create_user(db=db, user=user)
    return {"message": "createduser"}

@app.get("/users/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_smarthome_devices(db, skip=skip, limit=limit)
    return users

async def handle_data(data: str, db: Session): 
    try:
        json_data = json.loads(data)
        if "method" in json_data: 
            try: 
                fun = getattr(utils, f"handle_{json_data['method']}")
                return fun(json_data, db)
            except Exception as e: 
                logger.error(e)
                return get_internal_server_error(data)
            
    except Exception as e:
        logger.error(e) 
        logger.info(f"Can not handle {data}")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket): 
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            broadcast, out = await handle_data(data, next(get_db()))
            all_data = get_broadcast_data_dict(crud.get_all_data(db=next(get_db())))
            if broadcast: 
                await manager.broadcast(json.dumps(all_data))
            await manager.send_personal_message(json.dumps(out), websocket)
            
    except WebSocketDisconnect:
        logger.error("Lost a client")
        manager.disconnect(websocket)
        await manager.broadcast(json.dumps("Lost a Client")) 




class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()