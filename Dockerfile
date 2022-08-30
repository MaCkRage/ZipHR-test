FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install apt-utils && apt-get install -y gettext

COPY docker-entrypoint.sh /code/
COPY requirements.txt /code/

RUN pip3 install -r /code/requirements.txt

COPY example-prod.env /code/.env
COPY backend /code/backend/
COPY frontend /code/frontend/
COPY uploads /code/uploads/
COPY public /code/public/
