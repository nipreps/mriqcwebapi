import os
import re
get_mongo_host = re.match('tcp://(.*):(.*)', os.environ['MONGODB_PORT'])

my_settings = {
    'MONGO_HOST': get_mongo_host.group(1),
    'MONGO_PORT': get_mongo_host.group(2),
    'MONGO_DBNAME': 'scenarios',
    'X_DOMAINS': '*',
    'DOMAIN': {
        'scenarios': {
            'item_title': 'scenario',
            'resource_methods': ['GET', 'POST'],
            'item_methods': ['GET', 'PATCH', 'PUT', 'DELETE'],
            'schema': {
                'title': {
                    'type': 'string',
                    'minlength': 1,
                    'maxlength': 100,
                    'required': True
                }
            }
        }
    }
}

