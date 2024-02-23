from pydantic import BaseModel
from ..models.smarthome import SmarthomeDeviceChannelTypeEnum, IconEnum

class SmarthomeDeviceChannelBase(BaseModel): 
    channel_no: int
    type: SmarthomeDeviceChannelTypeEnum = SmarthomeDeviceChannelTypeEnum.INT
    
    class Config:
        orm_mode = True

class SmarthomeDeviceChannel(SmarthomeDeviceChannelBase): 
    id: int
    smarthomedevice_id: int

    class Config:
        orm_mode = True

class SmarthomeDeviceBase(BaseModel): 
    name: str 
    icon: IconEnum
    channels: list[SmarthomeDeviceChannelBase]

    class Config:
        orm_mode = True

class SmarthomeDevice(SmarthomeDeviceBase): 
    id: int

    class Config:
        orm_mode = True
    

    