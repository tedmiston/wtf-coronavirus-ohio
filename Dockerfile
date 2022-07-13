FROM python:3.9.13-slim@sha256:c01a2db78654c1923da84aa41b829f6162011e3a75db255c24ea16fa2ad563a0 AS base

WORKDIR /usr/src/app

RUN pip install --upgrade pip && pip install poetry --pre

COPY app ./app

COPY pyproject.toml .
COPY poetry.lock .

FROM base AS test
# RUN apt update && apt install tree && apt clean
RUN poetry install
CMD poetry run pytest --cov=app

FROM base AS prod
RUN poetry install --no-dev
CMD poetry run python -m app
