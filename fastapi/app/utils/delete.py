import logging 
from sql_app import models

logger = logging.getLogger(__name__)

def delete_smarthomedevice(data, db): 
    if "data" in data and "id" in data['data']: 
        id = data['data']['id']
        db.query(models.SmarthomeDeviceChannel).filter(models.SmarthomeDeviceChannel.smarthomedevice_id==id).delete(synchronize_session=False)
        db.query(models.SmarthomeDevice).filter(models.SmarthomeDevice.id == id).delete(synchronize_session=False)
        db.commit()

    return (True, {})

def delete_uielement(data, db): 
    if "data" in data and "id" in data['data']: 
        id = data['data']['id']
        db.query(models.Value).filter(models.Value.metauielement_id==id).delete(synchronize_session=False)
        db.query(models.MetaUIElement).filter(models.MetaUIElement.id == id).delete(synchronize_session=False)
        db.commit()

    return (True, {})

def delete_contextofuse(data,db): 
    if "data" in data and "id" in data['data']: 
        id = data['data']['id']
        db.query(models.ContextOfUse).filter(models.ContextOfUse.id == id).delete(synchronize_session=False)
        db.commit()
    
    return (True, {})

def delete_adaptui(data, db): 
    if "data" in data and "id" in data['data']: 
        id = data['data']['id']
        db.query(models.AdaptUIRule).filter(models.AdaptUIRule.id == id).delete(synchronize_session=False)
        db.commit()

    return (True, {})