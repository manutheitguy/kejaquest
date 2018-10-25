
 FROM python:3.7
 ENV PYTHONDONTWRITEBYTECODE 1
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /www
 WORKDIR /www
 ADD requirements.txt /www/
 RUN pip install -r requirements.txt
 ADD . /www/