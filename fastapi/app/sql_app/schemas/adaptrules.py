from pydantic import BaseModel
from ..models.adaptrules import ActionEnum

class ActionBase(BaseModel): 
    adaptui_id: int
    action: str 

class Action(ActionBase): 
    id: int


class ActionUIRuleBase(BaseModel): 
    name: str 
    level: str 
    actiongroup: ActionEnum
    actions: list[Action]