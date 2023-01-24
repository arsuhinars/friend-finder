
FROM python:3.11-alpine as base

WORKDIR /backend/

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv --no-cache-dir --disable-pip-version-check 

RUN pipenv install --system --deploy --ignore-pipfile


FROM base as prod

COPY app/ app/
