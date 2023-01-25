
# Base image
FROM python:3.11-alpine as base

ARG BACKEND_PORT=8000
ENV BACKEND_PORT=$BACKEND_PORT

WORKDIR /backend

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv --no-cache-dir --disable-pip-version-check 

RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE $BACKEND_PORT


# Development image
FROM base as development

CMD [ "sh", "-c", "uvicorn app.main:app --port $BACKEND_PORT --host 0.0.0.0 --reload" ]


# Production image
FROM base as production

COPY app/ app/

CMD [ "sh", "-c", "uvicorn app.main:app --port $BACKEND_PORT --host 0.0.0.0" ]
