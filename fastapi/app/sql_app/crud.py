from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select
from sqlalchemy.orm.collections import InstrumentedList
from utils.const import get_broadcast_data_dict
from . import models, schemas
import json 
from sql_app.models.adaptrules import OperatorEnum
import logging 

logger = logging.getLogger(__name__)
def get_smarthome_devices(db: Session, skip: int = 0, limit: int = 100) -> list: 
    # query_list =  db.query(models.SmarthomeDevice).options(joinedload(models.SmarthomeDevice.channels)).offset(skip).limit(limit).all()
    # out = []
    # for item in query_list: 
    #     temp_smarthomedevice_schema = schemas.SmarthomeDevice(**item.__dict__)
    #     out.append(json.loads(temp_smarthomedevice_schema.json()))

    query_list =  db.query(models.SmarthomeDevice).options(joinedload(models.SmarthomeDevice.channels)).all()
    out = []
    for item in query_list: 
        temp_smarthomedevice_schema = schemas.SmarthomeDevice(**item.__dict__)
        out.append(json.loads(temp_smarthomedevice_schema.json()))
    return out

def get_uielements(db: Session, skip: int = 0, limit: int = 100) -> list: 
    query_list = db.query(models.MetaUIElement).options(joinedload(models.MetaUIElement.values)).all()
    out = []
    for item in query_list: 
        temp_dict = item.__dict__
        temp_dict["values"] = [value.__dict__ for value in temp_dict["values"]]
        temp_uielement_schema = schemas.UIElement(**temp_dict)
        out.append(json.loads(temp_uielement_schema.json()))
    return out

def get_contextofuse(db: Session, skip: int = 0, limit: int = 100) -> list: 
    query_list = db.query(models.ContextOfUse).all()
    out = []
    for item in query_list: 
        temp_contextofuse_schema = schemas.ContextOfUse(**item.__dict__)
        out.append(json.loads(temp_contextofuse_schema.json()))
    return out

def get_adaptuirules(db: Session, skip: int = 0, limit: int = 100) -> list: 
    query_list = db.query(models.AdaptUIRule).options(
        joinedload(models.AdaptUIRule.create_actions), 
        joinedload(models.AdaptUIRule.delete_actions), 
        joinedload(models.AdaptUIRule.adjust_value_actions).subqueryload(models.AdjustValueViewAction.adjust_value), 
        joinedload(models.AdaptUIRule.layout_change_actions),
        joinedload(models.AdaptUIRule.orconditions).subqueryload(models.AdaptUIRuleORCondition.andconditions),
        joinedload(models.AdaptUIRule.influenced_context_of_use_vars), 
       
        ).all()
    out = []
    for item in query_list: 
        temp_dict = item.__dict__ 
        for key, value in temp_dict.items(): 
            t = type(value)
            if type(value) == InstrumentedList: 
                temp_dict[key] = [action.__dict__ for action in temp_dict[key]]
                tt = temp_dict[key]
                if type(temp_dict[key]) == list[InstrumentedList]: 
                    here = temp_dict[key]
                    pass
        for x in temp_dict["orconditions"]: 
            x["andconditions"]= [action.__dict__ for action in x["andconditions"]]
            
        for x in temp_dict["adjust_value_actions"]: 
            x["adjust_value"]= [action.__dict__ for action in x["adjust_value"]]
        # temp_dict['create_actions'] = [action.__dict__ for action in temp_dict['create_actions']]
        # temp_dict['influenced_context_of_use_vars'] = [action.__dict__ for action in temp_dict['influenced_context_of_use_vars']]
        temp_adaptuirule = schemas.AdaptUIRuleBase(**temp_dict)
        out.append(json.loads(temp_adaptuirule.json()))
    return out 

def get_smarthomeview(db: Session) -> list:
    query_list =  db.query(models.SmarthomeDevice).options(joinedload(models.SmarthomeDevice.channels).subqueryload(models.SmarthomeDeviceChannel.contextofuse)).all()
    out = []
    for item in query_list: 
        temp_dict = item.__dict__ 
        temp_dict['channels'] = [action.__dict__ for action in temp_dict['channels']]

        temp_smarthomeview = schemas.SmarthomeView(**temp_dict)
        out.append(json.loads(temp_smarthomeview.json()))


    return out        

def _compare(operator, a, b): 
    if operator == OperatorEnum.EQUAL: 
        return a == b 
    
    if operator == OperatorEnum.NOTEQUAL: 
        return a != b 
    
    if operator == OperatorEnum.GREATER: 
        return a > b 
    
    if operator == OperatorEnum.LOWER: 
        return a < b 
    
    if operator == OperatorEnum.GREATEREQUAL: 
        return a >= b 
    
    if operator == OperatorEnum.LOWEREQUAL: 
        return a <= b
    

def _cast_values(cast_type, a, b) -> tuple: 
    if cast_type == "STRING": 
        return (str(a), str(b))
    
    if cast_type == "INT": 
        return (int(a), int(b))

def _validate_rule_relevance(rule) -> bool:
    for orcondition in rule.orconditions: 
        valid = True
        for andcondition in orcondition.andconditions: 
            a, b = _cast_values(andcondition.contextofuse.type, andcondition.contextofuse.value, andcondition.value)
            if not _compare(andcondition.operator, a,b): 
                valid = False
        if valid: 
            return True
    return False 


def get_userview(db: Session) -> list: 

    query_adaptuirules = db.query(models.AdaptUIRule).options(
        joinedload(models.AdaptUIRule.orconditions).subqueryload(models.AdaptUIRuleORCondition.andconditions), 
        joinedload(models.AdaptUIRule.create_actions).subqueryload(models.CreateViewAction.metauielement).subqueryload(models.MetaUIElement.values).subqueryload(models.Value.contextofuse), 
        joinedload(models.AdaptUIRule.delete_actions),
        joinedload(models.AdaptUIRule.adjust_value_actions).subqueryload(models.AdjustValueViewAction.adjust_value).subqueryload(models.AdjustValue.metauielemeentvalues).subqueryload(models.Value.contextofuse),
    ).order_by(models.AdaptUIRule.level)
    relevant_rules = []
    for rule in query_adaptuirules: 
        if(_validate_rule_relevance(rule)): 
            relevant_rules.append(rule)
    
    uielements = []
    for rule in relevant_rules: 
        # step 1 creation
        uielements.extend([action.metauielement for action in rule.create_actions])
        # step 2 deletion 
        delete_ids = [daction.metauielement_id for daction in rule.delete_actions]
        for element in uielements: 
            if element.id in delete_ids: 
                uielements.remove(element)

        # step 3 adjust
        for avaction in rule.adjust_value_actions: 
            avaction.metauielement.min = avaction.min
            avaction.metauielement.max = avaction.max
            for avactionvalue in avaction.adjust_value: 
                avactionvalue.metauielemeentvalues.min = avactionvalue.min
                avactionvalue.metauielemeentvalues.max = avactionvalue.max
            # db.commit()
        

    out = []
    for item in uielements: 
        temp_dict = item.__dict__ 
        temp_dict['values'] = [action.__dict__ for action in temp_dict['values']]

        temp_uielementview = schemas.UIElementView(**temp_dict)
        out.append(json.loads(temp_uielementview.json()))
    return out


def get_all_data(db: Session): 
    return {
        'smarthomedevices': get_smarthome_devices(db), 
        'contextofuse': get_contextofuse(db), 
        'adaptuirules': get_adaptuirules(db), 
        'uielements': get_uielements(db), 
        'smarthomeview': get_smarthomeview(db), 
        'userview': get_userview(db)
    }
