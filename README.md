Built on:
* [Python Eve](http://python-eve.org/)
* [Python Gunicorn](http://gunicorn.org/)
* [Nginx](https://nginx.org/)
* [Docker](https://www.docker.com/)

## Run
Example of commands to run locally to start:
```sh
$ cd dockereve-master/
$ docker-compose build
$ docker-compose up -d
$ curl -i -H "Content-Type: application/json" http://localhost/api/v1/T1w
```

Swagger API documentation available at `http://localhost/docs`.

## Tests
### Integration (pytest)
These tests require a running Docker Compose stack and a valid API token.

Local run:
```sh
$ cd dockereve-master/
$ docker-compose up -d
$ cd ..
$ export API_TOKEN=<secret_token>
$ export MRIQC_API_BASE_URL=http://localhost
$ pytest -q -m integration
```

CI run (example):
```sh
$ docker compose -f dockereve-master/docker-compose.yml up -d
$ API_TOKEN=<secret_token> MRIQC_API_BASE_URL=http://localhost pytest -q -m integration
```

## Compatibility note (Python 3.7 base image)
The `dockereve-master/eve-app` image uses a Python 3.7 base. To avoid
`functools.cache` import errors from newer Flask/Werkzeug releases, the
`eve-app/requirements.txt` pins Eve to `1.1.5` and caps Flask/Werkzeug below
2.1. If you upgrade the runtime Python, revisit these pins accordingly.

## Environment variables in Docker
To properly run the file dockereve-master/.env needs to be populated the following are the default values:
```
MONGODB_HOST=mongodb
MONGODB_PORT=27017

API_TOKEN=<secret_token>
API_URL=http://localhost/docs/api
```

If docker is running natively these values should work, otherwise API_URL may need to be updated from localhost accordingly.
