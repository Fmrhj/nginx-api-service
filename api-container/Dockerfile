FROM python:3.6

LABEL MAINTAINER="Fhmrh https://github.com/Fmrhj/"

# Update
RUN apt-get update

# Install requirements
COPY ./requirements.txt /tmp/requirements.txt

WORKDIR /tmp
RUN pip3 install -r requirements.txt

# Copy app
WORKDIR /api-dir
COPY . /api-dir

# Change permissions to wrapper bash script 
RUN ls -l 
RUN chmod +x *.sh

# Start service with bash script
CMD "./start_api_service.sh"