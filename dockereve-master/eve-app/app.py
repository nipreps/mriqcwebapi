from eve import Eve
from settings import my_settings as ms
import os
script_dir = os.path.dirname(os.path.abspath(__file__))

from eve import Eve
from eve.auth import TokenAuth
from flask import current_app as app

class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        return token == '<secret_token>'

app = Eve(settings=ms, auth=TokenAuth)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

