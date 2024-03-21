from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PythonEnum
from ..database import Base

class UIElementEnum(str, PythonEnum): 
    BUTTON = 'BUTTON', 
    TOGGLEBUTTON = 'TOOGLEBUTTON', 
    SLIDER = 'SLIDER', 
    TRIANGLE = 'TRIANGLE'

class MetaUIElement(Base): 
    __tablename__ = "metauielement"
     
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    uielement = Column(Enum(UIElementEnum))
    current_value = Column(Integer)
    min = Column(Integer) 
    max = Column(Integer)
    step = Column(Integer)
    min_color = Column(String(7))
    max_color = Column(String(7))
    layoutlevel = Column(Integer)

    create_actions = relationship("CreateViewAction", back_populates="metauielement",cascade="all, delete", passive_deletes=True)
    delete_actions = relationship("DeleteViewAction", back_populates="metauielement",cascade="all, delete", passive_deletes=True)
    adjust_value_actions = relationship("AdjustValueViewAction", back_populates="metauielement",cascade="all, delete", passive_deletes=True)
    layout_change_actions = relationship("LayoutChangeAction", back_populates="metauielement",cascade="all, delete", passive_deletes=True)
    values = relationship("Value", back_populates="metauielement",cascade="all, delete", passive_deletes=True)
    adjust_value_actions = relationship("AdjustValueViewAction", cascade="all, delete", passive_deletes=True)

class Value(Base): 
    __tablename__ = "metauielemeentvalue"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    min = Column(Integer)
    max = Column(Integer)
    metauielement_id = Column(Integer, ForeignKey("metauielement.id", ondelete="CASCADE"))
    contextofuse_id = Column(Integer, ForeignKey("contextofuse.id", ondelete="CASCADE"))
    
    metauielement = relationship("MetaUIElement", back_populates="values")
    contextofuse = relationship("ContextOfUse", back_populates="metauielementvalues") 
    adjust_value_actions = relationship("AdjustValue", back_populates="metauielemeentvalues")
