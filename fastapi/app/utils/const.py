

def get_method_not_found(data): 
    return (
        False, 
            {
            'code': 405, 
            'message': "Method not found" , 
            'sended': data
            }
        )

def get_internal_server_error(data): 
    return (
        False ,
            {
            'code': 500, 
            'message': "internal error" 
            }
        )

def get_broadcast_data_dict(data): 
    return {
        'method': 'broadcast', 
        'type': 'data', 
        'data': data
    }