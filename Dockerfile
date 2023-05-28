FROM python:3.10-alpine

ARG run_request
ENV request $run_request


LABEL "Project name"="AutoTests of API"
LABEL "creator"="Nerodro"

WORKDIR C/Tests

COPY . .

RUN pip3 install -r requirements.txt

CMD pytest -s -v -k "$request" Tests/*

