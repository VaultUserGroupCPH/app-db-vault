FROM python:2.7

# Having this image makes it faster to rebuild pyapp because all the dependencies are inhere

RUN apt-get update
RUN pip install --upgrade pip

RUN apt-get install python-mysqldb
RUN pip install hvac flask MySQL-python

