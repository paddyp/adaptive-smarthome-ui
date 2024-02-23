from pydantic import BaseModel
from ..models.contextofuse import TypeEnum

class ContextOfUseBase(BaseModel): 
    key: str
    value: str 
    type: TypeEnum
    smarthomedevicechannel_id: int = None

class ContextOfUse(ContextOfUseBase): 
    id: int