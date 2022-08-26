FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y gettext && apt install -y ffmpeg

# На время разработки:
RUN apt install -y vim
# .

WORKDIR /code
COPY requirements.txt /code/
COPY requirements_base.txt /code/
COPY vendor /code/vendor/
RUN pip3 install -r /code/requirements.txt -r /code/requirements_base.txt

WORKDIR /code

COPY backend /code/backend/
COPY frontend /code/frontend/
COPY conf /code/conf

WORKDIR /code/backend

EXPOSE 8080
