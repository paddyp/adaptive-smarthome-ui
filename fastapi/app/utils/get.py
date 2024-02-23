from sql_app import schemas, models 
from utils.const import get_broadcast_data_dict
import logging 
logger = logging.getLogger(__name__)

schemas_dic = {
    "smarthome": schemas.SmarthomeDeviceBase.schema(), 
    "contextofuse": schemas.ContextOfUseBase.schema(), 
    "adaptrules": schemas.ActionUIRuleBase.schema(),  
}
def get_data(data, db): 
    pass

def get_schema(data, db): 
    _ = db
    if "schema" in data and data["schema"] in schemas_dic: 
        return (False, 
                {
                    'code': 200, 
                    'schema': schemas_dic[data["schema"]]
                })
    else: 
        # handle all schemas
        return (False, 
                {
                    'code': 200, 
                    'schemas': schemas_dic
                })

