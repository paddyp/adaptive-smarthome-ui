from utils.const import get_internal_server_error
from sql_app import schemas, models
import logging
from sql_app.helper import parse_pydantic_schema
from sqlalchemy.orm import joinedload


logger = logging.getLogger(__name__)

def _update_smarthomedevice_channels(db,smarthomedevice_id: int, channels: list): 
    # delete unused
    new_ids = [channel['id'] for channel in channels if "id" in channel]
    current_channels = db.query(models.SmarthomeDeviceChannel.id).filter(models.SmarthomeDeviceChannel.smarthomedevice_id == smarthomedevice_id).all()
    delteable_channels = [channel_id for (channel_id,) in current_channels if channel_id not in new_ids]
    db.query(models.SmarthomeDeviceChannel).filter(models.SmarthomeDeviceChannel.id.in_(delteable_channels)).delete()
    db.commit()

    
    
    for channel in channels: 
        # check if channel has -1 and create a new one 
        if "id" not in channel: 
            # create channel 
            channel["smarthomedevice_id"] = smarthomedevice_id
            temp_new_channel = models.SmarthomeDeviceChannel(**channel)
            db.add(temp_new_channel)
            db.commit()
        else: 
            db.query(models.SmarthomeDeviceChannel).filter(models.SmarthomeDeviceChannel.id == channel['id']).update(channel)
            db.commit()
        

def update_smarthomedevice(data, db): 
    if "data" in data and "id" in data["data"]: 
        id = data["data"]["id"]
        try: 
            channels = data["data"].pop("channels")
            _update_smarthomedevice_channels(db, smarthomedevice_id=id, channels=channels)
            db.query(models.SmarthomeDevice).filter(models.SmarthomeDevice.id == id).update(data["data"])
            return (True, {})

        except Exception as e: 
            logger.error(e)
            return get_internal_server_error(data)
def _update_values(db, meta_elementui_id, values): 
    # delete unused
    new_ids = [value['id'] for value in values if "id" in value]
    current_values = db.query(models.Value.id).filter(models.Value.metauielement_id == meta_elementui_id).all()
    delteable_channels = [value_id for (value_id,) in current_values if value_id not in new_ids]
    db.query(models.Value).filter(models.Value.id.in_(delteable_channels)).delete()
    db.commit()

    
    
    for value in values: 
        # check if channel has -1 and create a new one 
        if "id" not in value: 
            # create channel 
            value["metauielement_id"] = meta_elementui_id
            temp_new_value = models.Value(**value)
            db.add(temp_new_value)
            db.commit()
        else: 
            db.query(models.Value).filter(models.Value.id == value['id']).update(value)
            db.commit()

def update_uielement(data, db): 
    if "data" in data and "id" in data["data"]: 
        id = data["data"]["id"]
        try: 
            values = data["data"].pop("values")
            _update_values(db, meta_elementui_id=id, values=values)
            db.query(models.MetaUIElement).filter(models.MetaUIElement.id == id).update(data["data"])
            db.commit()
            return (True, {})

        except Exception as e: 
            logger.error(e)
            return get_internal_server_error(data)
        
def update_contextofuse(data, db): 
    try: 
        if "data" in data and "id" in data["data"]: 
            id = data["data"]["id"]
            db.query(models.ContextOfUse).filter(models.ContextOfUse.id == id).update(data["data"])
            db.commit()
            return (True, {})
    except Exception as e: 
        logger.error(e)
        return get_internal_server_error(data)
    
# def update_list(current_obj, new_object):
#     for  

def update_adaptui(data, db): 
    try:
        if "data" in data and "id" in data["data"]: 
            id = data["data"]["id"]
            orcondition = data["data"].pop("orconditions") if "orconditions" in data["data"] else []
            data["data"]["orconditions"] = []
            adaptui_schema = parse_pydantic_schema(schemas.AdaptUIRuleBase(**data["data"]))
            orconditions = []
            for condition in orcondition:
                or_condition_dict = parse_pydantic_schema(schemas.AdaptUIRuleORCondition(**condition))
                orconditions.append(models.AdaptUIRuleORCondition(**or_condition_dict))
            
            adaptui_schema["orconditions"] = orconditions
            model = models.AdaptUIRule(**adaptui_schema)
            db.query(models.AdaptUIRule).filter(models.AdaptUIRule.id == id).delete()
            db.add(model)
            db.commit()
            return (True, {})
        
    except Exception as e: 
        logger.error(e)
        return get_internal_server_error(data)

def update_data(data, db): 
    try: 
        id = data["data"]["id"]
        uielement = db.query(models.MetaUIElement).filter(models.MetaUIElement.id == id).first()
        uielement.current_value = data["data"]["current_value"]
        uielement_values = db.query(models.Value).filter(models.Value.metauielement_id == id).options(joinedload(models.Value.contextofuse)).all()
        percent = float(uielement.current_value) / 100.0
        for value, data_value in zip(uielement_values, data["data"]["values"]): 
            r = data_value["max"] - data_value["min"]
            new_value = str(int(data_value["min"] + (r * percent)))
            value.contextofuse.value = new_value
            for metauielementvalue in value.contextofuse.metauielementvalues: 
                metauielementvalue.metauielement.current_value = uielement.current_value
        db.commit()
        return (True, {})
    except Exception as e: 
        logger.error(e)
        return get_internal_server_error(data)
    pass