from pydantic import BaseModel
from ..models.adaptrules import ActionGroupEnum

class ActionBase(BaseModel): 
    adaptui_id: int
    action: str 

class Action(ActionBase): 
    id: int


class ActionUIRuleBase(BaseModel): 
    name: str 
    level: str 
    actiongroup: ActionGroupEnum
    actions: list[Action]