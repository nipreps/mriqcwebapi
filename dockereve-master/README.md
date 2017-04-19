# dockereve


## Overview
A sample Python Eve project with Python Gunicorn

Built on:
* [Python Eve](http://python-eve.org/)
* [Python Gunicorn](http://gunicorn.org/)
* [Nginx](https://nginx.org/)
* [Docker](https://www.docker.com/)

## Run
```sh
$ docker-compose build
$ docker-compose up
$ curl -H "Content-Type: application/json" -X POST -d '{"title": "Hello World"}' http://192.168.99.100:80/scenarios
$ curl -i -H "Content-Type: application/json" http://192.168.99.100:80/scenarios
```

## Contribution

### Creating Issues

If you find a problem please create an 
[issue in the ticket system](https://github.com/cpapazaf/dockereve/issues)
and describe what is going wrong or what you expect to happen.
If you have a full working example or a log file this is also helpful.
You should of course describe only a single issue in a single ticket and not 
mixing up several different things into a single issue.

### Creating a Pull Request

Before you create a pull request it is necessary to create an issue in
the [ticket system before](https://github.com/cpapazaf/dockereve/issues)
and describe what the problem is or what kind of feature you would like
to add. Afterwards you can create an appropriate pull request.

It is required if you want to get a Pull request to be integrated into to squash your
commits into a single commit which references the issue in the commit message.

A pull request has to fulfill only a single ticket and should never create/add/fix
several issues in one, cause otherwise the history is hard to read and to understand 
and makes the maintenance of the issues and pull request hard.

## License

Distributed under the Apache License 2.0 license: http://opensource.org/licenses/Apache-2.0
