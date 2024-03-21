from sql_app import schemas, models
from utils.const import get_internal_server_error
import logging
from sql_app.helper import parse_pydantic_schema
logger = logging.getLogger(__name__)

def create_smarthomedevice(data, db): 
    logger.info("inside of create smarthomedevice")
    try: 
        channels = data.pop("channels") # channels must be set 
        channel_models = []
        for channel in channels: 
            channel_schema_model = schemas.SmarthomeDeviceChannel(**channel)
            channel_models.append(
                models.SmarthomeDeviceChannel(**channel_schema_model.dict())
            )
        smarthome_device = models.SmarthomeDevice(**data)
        smarthome_device.channels = channel_models 
        db.add(smarthome_device)
        db.commit()
        return (True, {
            'code': 200, 
            'message': 'add smartdevice sucessfull',
            'sended': data
        })
    except Exception as e: 
        logger.error(e)
        return  get_internal_server_error(data)

def create_uielement(data, db): 
    logger.info("inside of create uielement")
    try: 
        values = data.pop("values") # min one value must be set 
        value_models = []
        for value in values: 
            value_schema_model = schemas.Value(**value)
            value_models.append(
                models.Value(**value_schema_model.dict())
            )
        uielement = models.MetaUIElement(**data)
        uielement.values = value_models
        db.add(uielement)
        db.commit()
        return (True, {
            'code': 200, 
            'message': 'add uielement sucessfull',
            'sended': data
        })
    except Exception as e: 
        logger.error(e)
        return get_internal_server_error(data)

def create_contextofuse(data, db): 
    logger.info("inside of create contextofuse")
    try:
        db.add(models.ContextOfUse(**data))
        db.commit()
        return (True, {
            'code': 200, 
            'message': 'add context of use successfully', 
            'sended': data
        })
        
    except Exception as e: 
        logger.error(e)
        return get_internal_server_error(data)
    
def create_adaptui(data, db): 
    logger.info("inside of create adaptui")
    try: 
        orcondition = data.pop("orconditions")
        adjust_value_actions = data.pop("adjust_value_actions")
        data["orconditions"] = []
        data["adjust_value_actions"] = []
        adaptui_schema = parse_pydantic_schema(schemas.AdaptUIRuleBase(**data))
        # 
        orconditions = []
        for condition in orcondition:
             or_condition_dict = parse_pydantic_schema(schemas.AdaptUIRuleORCondition(**condition))
             orconditions.append(models.AdaptUIRuleORCondition(**or_condition_dict))
        
        adaptui_schema["orconditions"] = orconditions

        adjust_value_actions_out = []
        for adjust_value_action in adjust_value_actions: 
            adjust_value_action_dict = parse_pydantic_schema(schemas.AdjustValueAction(**adjust_value_action))
            adjust_value_actions_out.append(models.AdjustValueViewAction(**adjust_value_action_dict))

        adaptui_schema["adjust_value_actions"] = adjust_value_actions_out
        model = models.AdaptUIRule(**adaptui_schema)
        db.add(model)
        db.commit()
        return (True, {
            'code': 200, 
            'message': 'add adaptui successfully', 
            'sended': data
        })
        
    except Exception as e:
        import traceback
 
        logger.error(e)
        logger.error(traceback.format_exc())
        return get_internal_server_error(data)   
