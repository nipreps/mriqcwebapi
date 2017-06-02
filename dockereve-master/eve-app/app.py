# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

import os

from eve import Eve
from eve.auth import TokenAuth
from eve_swagger import swagger
from settings import my_settings as ms

class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        return token == os.environ.get("API_TOKEN", '<secret_token>')

app = Eve(settings=ms, auth=TokenAuth)
app.register_blueprint(swagger, url_prefix='/docs/api')
app.add_url_rule('/docs/api', 'eve_swagger.index')

# required. See http://swagger.io/specification/#infoObject for details.
app.config['SWAGGER_INFO'] = {
    'title': 'MRIQC Web API',
    'version': '0.1',
    'description': 'MRI Quality Control Metrics Repository',
}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
