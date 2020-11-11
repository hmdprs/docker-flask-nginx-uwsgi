# use the python3.8 container image
FROM python:3.8

# set the working directory to /app
WORKDIR /app

# copy the current directory contents into the directory at /app
ADD . /app

# install the dependencies
RUN pip install -r requirements.txt

# run the command to start uWSGI
CMD [ "uwsgi", "app.ini" ]
