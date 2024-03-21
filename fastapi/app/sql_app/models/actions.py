from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship 

from ..database import Base


class CreateViewAction(Base): 
    __tablename__ = "createviewaction"

    id = Column(Integer, primary_key=True)
    metauielement_id = Column(Integer, ForeignKey("metauielement.id", ondelete="CASCADE"))
    adaptuirule_id = Column(Integer, ForeignKey("adaptuirule.id", ondelete="CASCADE"))


    metauielement = relationship("MetaUIElement", back_populates="create_actions", foreign_keys=[metauielement_id])
    adaptuirule = relationship("AdaptUIRule", back_populates="create_actions", foreign_keys=[adaptuirule_id])

class DeleteViewAction(Base): 
    __tablename__ = "deleteviewaction"

    id = Column(Integer, primary_key=True)
    metauielement_id = Column(Integer, ForeignKey("metauielement.id", ondelete="CASCADE"))
    adaptuirule_id = Column(Integer, ForeignKey("adaptuirule.id", ondelete="CASCADE"))


    metauielement = relationship("MetaUIElement", back_populates="delete_actions")
    adaptuirule = relationship("AdaptUIRule", back_populates="delete_actions")

class AdjustValueViewAction(Base): 
    __tablename__ = "adjustvalueviewaction"

    id = Column(Integer, primary_key=True)
    metauielement_id = Column(Integer, ForeignKey("metauielement.id", ondelete="CASCADE"))
    adaptuirule_id = Column(Integer, ForeignKey("adaptuirule.id", ondelete="CASCADE"))
    min = Column(Integer)
    max = Column(Integer)

    metauielement = relationship("MetaUIElement", back_populates="adjust_value_actions")
    adaptuirule = relationship("AdaptUIRule", back_populates="adjust_value_actions")
    adjust_value = relationship("AdjustValue", back_populates="adjust_value_action")

class AdjustValue(Base): 
    __tablename__ = "adjustvalue"

    id = Column(Integer, primary_key=True)
    adjust_value_action_id = Column(Integer, ForeignKey("adjustvalueviewaction.id", ondelete="CASCADE"))
    metauielemeentvalue_id = Column(Integer, ForeignKey("metauielemeentvalue.id", ondelete="CASCADE"))
    min = Column(Integer)
    max = Column(Integer)

    metauielemeentvalues = relationship("Value", back_populates="adjust_value_actions")
    adjust_value_action = relationship("AdjustValueViewAction", back_populates="adjust_value")

class LayoutChangeAction(Base): 
    __tablename__ = "layoutchangeaction"

    id = Column(Integer, primary_key=True)
    metauielement_id = Column(Integer, ForeignKey("metauielement.id", ondelete="CASCADE"))
    adaptuirule_id = Column(Integer, ForeignKey("adaptuirule.id", ondelete="CASCADE"))
    key = Column(String(100))
    value = Column(String(100))

    metauielement = relationship("MetaUIElement", back_populates="layout_change_actions")
    adaptuirule = relationship("AdaptUIRule", back_populates="layout_change_actions")