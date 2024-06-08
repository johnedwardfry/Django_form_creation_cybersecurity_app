#this is good for learning but typically you will want to specify a specific docker repo and image
# example 1: python:3.13.0b2-bookworm
# a registry maintained by the docker registry

# example 2: johnedwardfry:3.13.0b2-bookworm
# a registry maintained by an individual
FROM python:latest

# These are environment variables set for the os
# This does not allow python to create files locally allowing for a clean and stateless environment
ENV PYTHONDONTWRITEBYTECODE=true

# This puts stdout and stderr straight to terminal this prevents the loss of output in case python crashes
ENV PYTHONUNBUFFERED=true

# WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it
# in the Dockerfile. this is recommended as if it is not set you will have to specify the directory by running the cd
# command each time you use these commands.
WORKDIR /code

# This command will copy the code that is in the location of the DOCKERFILE into the /code directory inside the
# container this allows the code to run in an isolated container and will be accessed by the docker compose.yaml to
# build our webapp
COPY . /code/

# This runs a command in the os because we are using a linux base image these will be bash commands in this case it is
# getting the latest version of pip a python package installer and installing all of the packages listed in the
# requirements.txt file
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
