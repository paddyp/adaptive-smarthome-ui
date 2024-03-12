import logging
from utils import create, get, delete, update
from utils.const import get_method_not_found
logger = logging.getLogger(__name__)

def handle_create(data, db): 
    logger.info("handle create")
    out =  get_method_not_found(data)
    if "type" in data and "data" in data: 
        try: 
            fun = getattr(create, f"create_{data['type']}")
            out = fun(data["data"], db)
        except Exception as e: 
            logger.error(e)

    return out

def handle_get(data, db): 
    out = get_method_not_found(data)

    if "type" in data: 
        try: 
            fun = getattr(get, f"get_{data['type']}")
            out = fun(data, db)
        except Exception as e: 
            logger.error(e)

    return out

def handle_delete(data, db): 
    out = get_method_not_found(data)
    if "type" in data: 
        try: 
            fun = getattr(delete, f"delete_{data['type']}")
            out = fun(data, db)
        except Exception as e: 
            logger.error(e)

    return out

def handle_update(data, db): 
    out = get_method_not_found(data) 
    if "type" in data: 
        try: 
            fun = getattr(update, f"update_{data['type']}")
            out = fun(data, db)
        except Exception as e: 
            logger.error(e)
    return out

