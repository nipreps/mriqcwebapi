from eve import Eve
from settings import my_settings as ms
import os
script_dir = os.path.dirname(os.path.abspath(__file__))


app = Eve(settings=ms)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

