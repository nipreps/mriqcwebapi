FROM python:3.4-onbuild
WORKDIR /usr/src/app
RUN pip3 install pytest
COPY requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

COPY ./app /usr/src/app
