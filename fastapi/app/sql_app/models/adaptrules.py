from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from enum import Enum as PythonEnum

from ..database import Base

class ActionGroupEnum(str, PythonEnum): 
    TASKCHANGE = 'TASKCHANGE', 
    LAYOUTCHANGE = 'LAYOUTCHANGE', 
    SERVICE = 'SERVICE'

class ActionEnum(str, PythonEnum):
    ADDVIEWCOMPONENT = 'ADDVIEWCOMPONENT' 
    DELETEVIEWCOMPOENT = 'DELETEVIEWCOMPOENT'
    CREATEVIEWCOMPONENT = 'CREATEVIEWCOMPONENT'
    LAYOUTCHANGE = 'LAYOUTCHANGE' 
    SETDISPLAYPROPERTY = 'SETDISPLAYPROPERTY'
    SERVICEFUNCTIONCALL = 'SERVICEFUNCTIONCALL'

class OperatorEnum(str, PythonEnum): 
    EQUAL = "EQUAL", 
    NOTEQUAL = "NOTEQUAL", 
    GREATER = "GREATER",
    LOWER = "LOWER",
    GREATEREQUAL = "GREATEREQUAL",
    LOWEREQUAL = "LOWEREQUAL"

class TypeEnum(str, PythonEnum): 
    INT = "INT", 
    FLOAT = "FLOAT", 
    STRING = "STRING", 
    OBJECT = "OBJECT"

class AdaptUIRule(Base): 
    __tablename__ = "adaptuirule" 

    id = Column(Integer, primary_key=True)
    name = Column(String(100),)
    level = Column(Integer, index=True)
    explaination = Column(Text)
    explaination_level = Column(Integer)

    create_actions = relationship("CreateViewAction",  back_populates="adaptuirule", cascade="all, delete", passive_deletes=True)
    delete_actions = relationship("DeleteViewAction", back_populates="adaptuirule", cascade="all, delete", passive_deletes=True)
    adjust_value_actions = relationship("AdjustValueViewAction", back_populates="adaptuirule", cascade="all, delete", passive_deletes=True)
    layout_change_actions = relationship("LayoutChangeAction", back_populates="adaptuirule",cascade="all, delete", passive_deletes=True)

    influenced_context_of_use_vars = relationship("AdaptUIRuleInfluencedContextVar", back_populates="adaptuirule",cascade="all, delete", passive_deletes=True)
    orconditions = relationship("AdaptUIRuleORCondition", back_populates="adaptuirule", cascade="all, delete", passive_deletes=True,)

class AdaptUIRuleInfluencedContextVar(Base): 
    __tablename__ = "adaptuiruleinfluencedcontextvars"
    
    id = Column(Integer, primary_key=True)
    adaptuirule_id = Column(Integer, ForeignKey("adaptuirule.id", ondelete="CASCADE"))
    contextofuse_id = Column(Integer, ForeignKey("contextofuse.id", ondelete="CASCADE"))

    adaptuirule = relationship("AdaptUIRule", back_populates="influenced_context_of_use_vars")
    contextofuse = relationship("ContextOfUse")

class AdaptUIRuleORCondition(Base): 
    __tablename__ = "adaptuiruleorcondition"

    id = Column(Integer, primary_key=True)
    adaptuirule_id = Column(Integer, ForeignKey("adaptuirule.id", ondelete="CASCADE"))

    adaptuirule = relationship("AdaptUIRule", back_populates="orconditions")
    andconditions = relationship("AdaptUIRuleANDCondition", back_populates="orcondition", cascade="all, delete", passive_deletes=True,)

class AdaptUIRuleANDCondition(Base): 
    __tablename__ = "adaptuiruleandcondition"

    id = Column(Integer, primary_key=True)
    orcondition_id = Column(Integer, ForeignKey("adaptuiruleorcondition.id", ondelete="CASCADE"))

    contextvar_id = Column(Integer, ForeignKey("contextofuse.id", ondelete="CASCADE"))
    operator = Column(Enum(OperatorEnum))
    value = Column(String(255))

    orcondition = relationship("AdaptUIRuleORCondition")
    contextofuse = relationship("ContextOfUse")




    
