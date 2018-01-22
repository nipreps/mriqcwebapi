# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

import os

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
    'description': """<p>####################################################<br />
Because of a lapse in government funding, the information on this website 
may not be up to date, transactions submitted via the website may not be 
processed, and the agency may not be able to respond to inquiries until 
appropriations are enacted.<br />
The NIH Clinical Center (the research hospital of NIH) is open. For more details
about its operating status, please visit cc.nih.gov.<br />
####################################################<br />
    <a href="http://mriqc.org">MRIQC</a> is an open-source tool that extracts 
no-reference image quality metrics from structural and 
functional MRI data developed by the <a href="http://poldracklab.stanford.edu"> 
Poldrack Lab</a> at <a href="http://www.stanford.edu">Stanford University</a>. 
This website provides an api to a crowdsourced repository of MRI quality 
metrics contributed by users of MRIQC and hosted by 
the <a href="http://cmn.nimh.nih.gov">Data Science and Sharing Team</a> 
at the <a href="http://nimh.nih.gov">National Institute of Mental Health</a>.</p>""",
}

if os.environ.get('SWAGGER_HOST', None):
    app.config['SWAGGER_HOST'] = os.environt.get('SWAGGER_HOST')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
