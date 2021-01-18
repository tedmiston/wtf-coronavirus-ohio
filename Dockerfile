FROM python:3.9.1-slim@sha256:bb3926b0086410563a5c1da1b2dad6681d3088ebe0910308687c79f8f95c50bb AS base

WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install poetry

COPY . .

FROM base AS test
RUN poetry install
CMD [ "poetry", "run", "coverage", "run", "--source=.", "--omit=tests/*.py", "-m", "pytest" ]

FROM base AS prod
RUN poetry install --no-dev
CMD [ "poetry", "run", "python", "-m", "app" ]
