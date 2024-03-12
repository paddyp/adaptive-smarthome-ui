from pydantic import BaseModel
from ..models.smarthome import SmarthomeDeviceChannelTypeEnum, IconEnum
from .contextofuse import ContextOfUse
from sql_app import models 

class SmarthomeDeviceChannel(BaseModel): 
    id: int = None
    channel_no: int
    type: SmarthomeDeviceChannelTypeEnum
    contextofuse_id: int = None

    class Config:
        orm_mode = True
        orm_model = models.SmarthomeDeviceChannel


class SmarthomeDevice(BaseModel): 
    id: int = None
    name: str 
    icon: IconEnum
    channels: list[SmarthomeDeviceChannel]

    class Config:
        orm_mode = True
        orm_model = models.SmarthomeDevice


class SmarhomeViewChannel(BaseModel): 
    id: int = None
    channel_no: int
    type: SmarthomeDeviceChannelTypeEnum
    contextofuse: ContextOfUse = None

class SmarthomeView(BaseModel): 
    id: int = None
    name: str 
    icon: IconEnum
    channels: list[SmarhomeViewChannel]
    

    