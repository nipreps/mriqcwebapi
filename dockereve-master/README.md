Built on:
* [Python Eve](http://python-eve.org/)
* [Python Gunicorn](http://gunicorn.org/)
* [Nginx](https://nginx.org/)
* [Docker](https://www.docker.com/)

## Run
Example of commands to run locally to start:
```sh
$ docker-compose build
$ docker-compose up -d
$ curl -i -H "Content-Type: application/json" http://localhost/api/v1/T1w
```

Swagger API documentation available at `http://localhost/docs`.

## Environment variables in Docker
To properly run the file dockereve-master/.env needs to be populated the following are the default values:
```
MONGODB_HOST=mongodb
MONGODB_PORT=27017

API_TOKEN=<secret_token>
API_URL=http://localhost/docs/api
```

If docker is running natively these values should work, otherwise API_URL may need to be updated from localhost accordingly.
