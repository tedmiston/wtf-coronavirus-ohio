FROM python:3.9.2-slim@sha256:bb8911d79f5451a03748e65ec8944504b71ac09722c7ddbc5742daf7465a32c1 AS base

WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install poetry

# see `.dockerignore` for whitelisted files
COPY . .

FROM base AS test
RUN poetry install
CMD [ "poetry", "run", "coverage", "run", "--source=.", "--omit=tests/*.py", "-m", "pytest" ]

FROM base AS prod
RUN poetry install --no-dev
CMD [ "poetry", "run", "python", "-m", "app" ]
