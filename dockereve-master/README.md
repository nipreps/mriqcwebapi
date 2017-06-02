Built on:
* [Python Eve](http://python-eve.org/)
* [Python Gunicorn](http://gunicorn.org/)
* [Nginx](https://nginx.org/)
* [Docker](https://www.docker.com/)

## Run
```sh
$ docker-compose build
$ docker-compose up
$ curl -i -H "Content-Type: application/json" http://192.168.99.100:80/T1w
```

Swagger API documentation available at `http://localhost/docs`.

## Environment variables in Docker
To properly run the file dockereve-master/.env needs to be created and populated with the following values:
```
MONGODB_HOST=full url to mongodb host
MONGODB_PORT=port that mongo is running on
API_TOKEN=random string that is used for auth
API_URL=full url to swagger docs in the api
```
