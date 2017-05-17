FROM python:3.4
ENV PYTHONUNBUFFERED 1

MAINTAINER Artem Bernatskyi <artem.bernatskyy@gmail.com>
ENV INSTALL_PATH /app/code


RUN mkdir -p $INSTALL_PATH
WORKDIR ${INSTALL_PATH}

RUN mkdir /app/config  
COPY requirements.txt /app/config/
RUN pip install -r /app/config/requirements.txt

COPY ./compose/django/gunicorn.sh /app/config/gunicorn.sh
RUN chmod +x /app/config/gunicorn.sh 

COPY . ${INSTALL_PATH}
