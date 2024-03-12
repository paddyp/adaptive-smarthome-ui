from pydantic import BaseModel
from ..models.contextofuse import TypeEnum
from sql_app import models

class ContextOfUse(BaseModel): 
    id: int = None
    key: str
    value: str 
    type: TypeEnum
    
    class Config:
        orm_mode = True
        orm_model = models.ContextOfUse

