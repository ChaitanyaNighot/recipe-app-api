FROM python:3.9.0-alpine
MAINTAINER Chaitanya (Numino Labs)

#PYTHONUNBUFFERED is added so that python will not buffer
#output and will print it, adviced for when using docker.
ENV PYTHONUNBUFFERED 1

#requirements will have list of all the modules that needs to be installed
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

#create app folder in container and place source files there
RUN mkdir /app
#make this app folder as default folder
WORKDIR /app
COPY ./app /app

#create a user in container which will have rights only to run the application
RUN adduser -D user
#switch user in container to newly created user
USER user