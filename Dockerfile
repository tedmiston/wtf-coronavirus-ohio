FROM python:3.8.2-slim@sha256:c0281d8fe99edff517fcc748f088bc51822ae660bac9e4aba76a81fa987fe9e8 AS base
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
