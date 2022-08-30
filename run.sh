#!/usr/bin/env bash
BULD="$1"

if [[ $BULD == "-h" ]] || [[ $BULD == "--help" ]]
then
  echo "
  params of bulding:
    - test: web will start in global
    - prod: web will start in container
  "

elif [[ $BULD == "test" ]]; then

  cp example.env .env

  # is venv
  if [ -d venv ]; then
    echo 'venv exists'
  else
    virtualenv -p python3.7 venv
    source venv/bin activate
    pip install --upgrade virtualenv
    python -m pip install --upgrade pip
    pip install -r requirements.txt
  fi

  docker-compose up -d
  python backend/manage.py migrate
  python code/backend/manage.py fill_db
  python backend/manage.py runserver

elif [[ $BULD == "prod" ]]; then
  cp example-prod.env .env
  docker-compose -f docker-compose-prod.yml build --progress=plain
  docker-compose -f docker-compose-prod.yml up -d
else
  echo "You need set a parameter test or prod. See --help"
fi
