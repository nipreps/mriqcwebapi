FROM python:3.4-onbuild

WORKDIR /usr/src/app

ADD . /usr/src/app

RUN pip3 install -r requirements.txt
RUN pip3 install pytest

#EXPOSE 5000
#CMD ["python3", "server.py"]

