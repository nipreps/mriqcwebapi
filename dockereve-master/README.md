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