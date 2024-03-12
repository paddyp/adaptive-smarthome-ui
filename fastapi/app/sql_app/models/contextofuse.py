from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PythonEnum

from ..database import Base

class TypeEnum(str, PythonEnum): 
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

    metauielementvalues = relationship("Value", back_populates="contextofuse", cascade="all, delete", passive_deletes=True)


