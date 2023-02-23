FROM python:3.7-slim

WORKDIR /usr/src/app

ADD . /usr/src/app

RUN pip3 install -r requirements.txt
RUN pip3 install pytest
RUN sed -i 's/\[scheme\]/\["https"\]/' /usr/local/lib/python3.7/site-packages/eve_swagger/objects.py
