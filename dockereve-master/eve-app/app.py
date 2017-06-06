# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

import os
import socket

from eve import Eve
from eve.auth import TokenAuth
from eve_swagger import swagger
from settings import settings

API_TOKEN = os.environ.get("API_TOKEN")

class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        return token == API_TOKEN

app = Eve(settings=settings, auth=TokenAuth)
app.register_blueprint(swagger, url_prefix='/docs/api')
app.add_url_rule('/docs/api', 'eve_swagger.index')

# required. See http://swagger.io/specification/#infoObject for details.
app.config['SWAGGER_INFO'] = {
    'title': 'MRIQC Web API',
    'version': 'v1',
    'description': 'MRI Quality Control Metrics Repository',
}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
