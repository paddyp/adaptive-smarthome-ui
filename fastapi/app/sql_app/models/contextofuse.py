from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PythonEnum

from ..database import Base

class TypeEnum(PythonEnum): 
    INT = 'INT', 
    FLOAT = 'FLOAT', 
    STRING = 'STRING', 
    JSON = 'JSON', 
    DEVICE = 'DEVICE'
    # extend for more 


class ContextOfUse(Base): 
    __tablename__ = "contextofuse" 

    id = Column(Integer, primary_key=True)
    key = Column(String(255), index=True)
    value = Column(String(255), index=True)
    type = Column(Enum(TypeEnum))
    smarthomedevicechannel_id = Column(Integer, ForeignKey("smarthomedevicechannel.id"))

    smarthomedevicechannel = relationship("SmarthomeDeviceChannel", back_populates="contextofuse")

