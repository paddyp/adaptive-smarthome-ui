from sql_app import schemas, models
from utils.const import get_internal_server_error
import logging
logger = logging.getLogger(__name__)

def create_smarthomedevice(data, db): 
    logger.info("inside of create smarthomedevice")
    try: 
        channels = data.pop("channels") # channels must be set 
        channel_models = []
        for channel in channels: 
            channel_schema_model = schemas.SmarthomeDeviceChannelBase(**channel)
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
