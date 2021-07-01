FROM python:3.9

RUN apt-get update -y && apt-get upgrade -y

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/