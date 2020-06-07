FROM python:3.6

LABEL MAINTAINER="Fhmrh https://github.com/Fmrhj/"

# Update
RUN apt-get update

# Install requirements
COPY ./requirements.txt /tmp/requirements.txt

WORKDIR /tmp
RUN pip3 install -r requirements.txt

# Copy app
WORKDIR /api
COPY . /api

# Change permissions to wrapper bashz script 
RUN ls -l 
RUN chmod a+x *.sh

WORKDIR /
RUN ls -l

# Start service with bash script: gunicorn configuration are detailed here
CMD [". api/start_api_service.sh"]