FROM python:3.6-onbuild

WORKDIR /usr/src/app

ADD . /usr/src/app

RUN pip3 install -r requirements.txt
RUN pip3 install pytest
RUN sed -i 's/\[scheme\]/\["https"\]/' /usr/local/lib/python3.6/site-packages/eve_swagger/objects.py

#EXPOSE 5000
#CMD ["python3", "server.py"]

