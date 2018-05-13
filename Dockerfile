FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /djangoproj
WORKDIR /djangoproj
ADD requirements.txt /djangoproj/
RUN pip install django
RUN pip install psycopg2
RUN pip install psycopg2-binary
ADD . /djangoproj/
