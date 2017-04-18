

MONGO_HOST = 'localhost'    
MONGO_PORT = 27017


MONGO_DBNAME = 'data'

ITEM_METHODS = ['GET','PUT']

RESOURCE_METHODS = ['GET', 'POST']


datas = {
    
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name'
    },
    
    'schema':{
    
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15
            'unique': True,
        },
    }
}

DOMAIN = {'test': datas,}
