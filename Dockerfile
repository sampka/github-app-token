# Container image that runs your code
FROM python:3

COPY requirements.txt /requirements.txt

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY app_authentication.py app/
COPY entrypoint.sh app/
COPY getinfo.py app/
RUN chmod u+x app/entrypoint.sh

WORKDIR /app

# Code file to execute when the docker container starts up
CMD /app/entrypoint.sh