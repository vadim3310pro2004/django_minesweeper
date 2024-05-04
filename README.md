# Minesweeper

Server layer for minesweeper game application

## To setup

1. install postgresql, redis, python

1. ```bach
    python -m pip install -U poetry
    ```

1. ```bach
    python -m poetry install
    ```

1. define in your evieron
    + SECRET_KEY
    + FRONTEND_ORIGINS
    + DEBUG
    + EMAIL_HOST
    + EMAIL_HOST_USER
    + EMAIL_HOST_PASSWORD
    + EMAIL_PORT
    + DB_ENGINE
    + DB_NAME
    + DB_USER
    + DB_PASSWORD
    + DB_HOST
    + DB_PORT
    + REDIS_URL
    + GOOGLE_OAUTH2_CLIENT_ID
    + ACCESS_TOKEN_LIFE_MINUTES
    + REFRESH_TOKEN_LIFE_DEYS
    + ALLOWED_HOSTS

## To run

1. ```bach
    cd backend
    python -m poetry shell
    ```

1. ```bach
    python manage.py migrate
    ```

1. ```bach
    celery -A backend worker --loglevel=INFO --pool=solo
    ```

1. ```bach
    celery -A backend flower
    ```

1. ```bach
    python manage.py runserver
    ```
