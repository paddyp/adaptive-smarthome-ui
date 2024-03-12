from sql_app import schemas, models 
from utils.const import get_broadcast_data_dict
from sql_app import crud
from sqlalchemy.orm import joinedload
import logging 
import json 

logger = logging.getLogger(__name__)

schemas_dic = {
    "smarthome": schemas.SmarthomeDevice.schema(), 
    "contextofuse": schemas.ContextOfUse.schema(), 
    "adaptrules": schemas.AdaptUIRuleBase.schema(),  
    "uielement": schemas.UIElement.schema(),
}
def get_data(data, db): 
    _ = data
    # query_list =  db.query(models.SmarthomeDevice).options(joinedload(models.SmarthomeDevice.channels)).all()
    # out = []
    # for item in query_list: 
    #     temp_smarthomedevice_schema = schemas.SmarthomeDevice(**item.__dict__)
    #     out.append(json.loads(temp_smarthomedevice_schema.json()))
    out = get_broadcast_data_dict(crud.get_all_data(db))
    return (False, out)

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
                    'type': 'schema',
                    'schemas': schemas_dic
                })

