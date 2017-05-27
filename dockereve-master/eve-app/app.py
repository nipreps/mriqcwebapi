from eve import Eve
from eve_swagger import swagger
from settings import my_settings as ms
import os
script_dir = os.path.dirname(os.path.abspath(__file__))

app = Eve(settings=ms)
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

