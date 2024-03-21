from pydantic import BaseModel
from ..models.adaptrules import OperatorEnum
from typing import Union, List
from sql_app import models

class ActionBase(BaseModel): 
    id: int = None 
    metauielement_id: int
    adaptuirule_id: int = None 

class CreateViewAction(ActionBase): 
    pass

    class Meta: 
        orm_model = models.CreateViewAction


class DeleteViewAction(ActionBase): 
    pass
    
    class Meta: 
        orm_model = models.DeleteViewAction

class AdjustValue(BaseModel): 
    id: int = None
    adjust_value_action_id: int = None
    metauielemeentvalue_id: int
    min: int 
    max: int 

    class Meta: 
        orm_model = models.AdjustValue

class AdjustValueAction(BaseModel): 
    id: int = None 
    metauielement_id: int
    adaptuirule_id: int = None
    adjust_value: list[AdjustValue] = [] 

    min: int 
    max: int

    class Meta: 
        orm_model = models.AdjustValueViewAction



class LayoutChangeAction(ActionBase): 
    key: str 
    value: str

    class Meta: 
        orm_model = models.LayoutChangeAction

class InfluencedContextOfUseVars(BaseModel): 
    id: int = None 
    contextofuse_id: int

    class Meta: 
        orm_model = models.AdaptUIRuleInfluencedContextVar


class AdaptUIRuleANDCondition(BaseModel): 
    id: int = None 
    orcondition_id: int = None
    contextvar_id: int  
    operator: OperatorEnum
    value: str

    class Meta: 
        orm_model = models.AdaptUIRuleANDCondition

class AdaptUIRuleORCondition(BaseModel): 
    id: int = None 
    adaptuirule_id: int = None
    andconditions: list[AdaptUIRuleANDCondition]

    class Meta: 
        orm_model = models.AdaptUIRuleORCondition

class AdaptUIRuleBase(BaseModel): 
    id: int = None
    name: str 
    level: str 
    explaination: str
    explaination_level: int

    create_actions: list[CreateViewAction] = []
    delete_actions: list[DeleteViewAction] = []
    adjust_value_actions: list[AdjustValueAction] = []
    layout_change_actions: list[LayoutChangeAction] = [] 

    influenced_context_of_use_vars: list[InfluencedContextOfUseVars] = []
    orconditions: list[AdaptUIRuleORCondition] = []


    class Config:
        orm_mode = True
        orm_model = models.AdaptUIRule