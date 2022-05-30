FROM ubuntu:18.04

MAINTAINER Emilio  "emilio.cimino@outlook.it"

RUN apt-get update -y 
RUN apt-get install -y python3-pip python3-dev 
RUN pip3 install --upgrade pip


COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN useradd app


COPY license.txt broker.proto broker_pb2.py broker_pb2_grpc.py AudioFileBroker.py ./app/
WORKDIR /app/
RUN chown -R app:app /app
RUN chmod 755 /app

USER app

ENTRYPOINT [ "python3","AudioFileBroker.py" ]
