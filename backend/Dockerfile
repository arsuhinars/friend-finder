
# Base image
FROM python:3.11-slim as base

ARG BACKEND_PORT=8000
ENV BACKEND_PORT=$BACKEND_PORT

WORKDIR /backend

# Install python packages
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv --no-cache-dir --disable-pip-version-check 
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE $BACKEND_PORT

# Add entrypoint script
COPY docker-entrypoint.sh /backend/docker-entrypoint.sh
ENTRYPOINT [ "/backend/docker-entrypoint.sh" ]

# Development image
FROM base as development

CMD [ "--reload" ]


# Production image
FROM base as production

COPY app/ app/
