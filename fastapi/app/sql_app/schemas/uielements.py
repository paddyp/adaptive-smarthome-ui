from pydantic import BaseModel 
from ..models.uielements import UIElementEnum
from .contextofuse import ContextOfUse
from sql_app import models

class Value(BaseModel): 
    id: int = None
    name: str 
    contextofuse_id: int   
    min: int
    max: int

    class Meta: 
        orm_model = models.Value

class UIElement(BaseModel): 
    id: int = None
    name: str 
    uielement: UIElementEnum
    current_value: int
    min: int 
    max: int
    min_color: str
    max_color: str
    layoutlevel: int
    values: list[Value]

    class Meta: 
        orm_model = models.MetaUIElement



class ViewValue(BaseModel): 
    id: int = None
    name: str
    contextofuse: ContextOfUse 
    min: int
    max: int

class UIElementView(UIElement): 
    values: list[ViewValue]