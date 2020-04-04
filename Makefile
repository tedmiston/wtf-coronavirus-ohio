.PHONY: build coverage format format-dry-run push run test

NAME=tedmiston/wtf-covid-19-ohio
TAG=latest
IMAGE=$(NAME):$(TAG)

build:
	@DOCKER_BUILDKIT=1 docker build --tag=$(IMAGE) .

run:
	@docker run --rm $(IMAGE)

test:
	@pipenv run coverage run --source=. --omit=tests/test_app.py -m pytest

coverage:
	@coverage report

format-dry-run:
	@black --diff .

format:
	@black .

push:
	@docker push $(IMAGE)
