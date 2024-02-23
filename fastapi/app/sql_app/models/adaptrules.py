from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from enum import Enum as PythonEnum

from ..database import Base

class ActionGroupEnum(PythonEnum): 
    TASKCHANGE = 'TASKCHANGE', 
    LAYOUTCHANGE = 'LAYOUTCHANGE', 
    SERVICE = 'SERVICE'

class ActionEnum(PythonEnum):
    ADDVIEWCOMPONENT = 'ADDVIEWCOMPONENT' 
    DELETEVIEWCOMPOENT = 'DELETEVIEWCOMPOENT'
    CREATEVIEWCOMPONENT = 'CREATEVIEWCOMPONENT'
    LAYOUTCHANGE = 'LAYOUTCHANGE' 
    SETDISPLAYPROPERTY = 'SETDISPLAYPROPERTY'
    SERVICEFUNCTIONCALL = 'SERVICEFUNCTIONCALL'

class AdaptUIRule(Base): 
    __tablename__ = "adaptuirule" 

    id = Column(Integer, primary_key=True)
    name = Column(String(100),)
    level = Column(Integer, index=True)
    actiongroup = Column(Enum(ActionGroupEnum))

    actions = relationship("Action", back_populates="rules")

class Action(Base): 
    __tablename__ = "action"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    adaptui_id = Column(Integer, ForeignKey("adaptuirule.id"))
    action = Column(Text)

    rules = relationship("AdaptUIRule", back_populates="actions")

