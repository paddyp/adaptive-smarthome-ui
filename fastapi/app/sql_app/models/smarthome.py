from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PythonEnum


from ..database import Base


### Enum-Defintions 

class IconEnum(str, PythonEnum): 
    LAMP = 'LAMP', 
    HEATER = 'HEATER', 
    SHUTTER = 'SHUTTER'


class SmarthomeDeviceChannelTypeEnum(str, PythonEnum): 
    INT = 'INT', 
    FLOAT = 'FLOAT'
    COLOR_RED = 'COLOR_RED', 
    COLOR_GREEN = 'COLOR_GREEN'
    COLOR_BLUE = 'COLOR_BLUE'
    DIMMER = 'DIMMER'

class SmarthomeDevice(Base): 
    __tablename__ = "smarthomedevice"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), )
    icon = Column(Enum(IconEnum))

    channels = relationship("SmarthomeDeviceChannel", back_populates="smarthomedevices")

    def as_dict(self):
       out =  {c.name: getattr(self, c.name) for c in self.__table__.columns}
       out["channels"] = [self.channels]
    

class SmarthomeDeviceChannel(Base): 
    __tablename__ = "smarthomedevicechannel"

    id = Column(Integer, primary_key=True)
    channel_no = Column(Integer)
    smarthomedevice_id = Column(Integer, ForeignKey("smarthomedevice.id"))
    type = Column(Enum(SmarthomeDeviceChannelTypeEnum))

    smarthomedevices = relationship("SmarthomeDevice", back_populates="channels", foreign_keys=[smarthomedevice_id])
    contextofuse = relationship("ContextOfUse", back_populates="smarthomedevicechannel")

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}