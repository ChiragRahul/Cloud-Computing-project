FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install python3 python3-pip mongo-tools

WORKDIR /worker
COPY . /worker

ENV TEAM_NAME=CC_2146_2161_2361

RUN pip3 install -r requirements.txt
