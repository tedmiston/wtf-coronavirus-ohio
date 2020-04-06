NAME=tedmiston/wtf-covid-19-ohio
TAG=latest
IMAGE=$(NAME):$(TAG)

.PHONY: build
build:
	@DOCKER_BUILDKIT=1 docker build --tag=$(IMAGE) .

.PHONY: run
run:
	@docker run --rm $(IMAGE)

.PHONY: test
test:
	@poetry run coverage run --source=. --omit=tests/test_app.py -m pytest

.PHONY: coverage
coverage:
	@coverage report

.PHONY: coverage-html
coverage-html:
	@coverage html

.PHONY: format-dry-run
format-dry-run:
	@black --diff .

.PHONY: format
format:
	@black .

.PHONY: push
push:
	@docker push $(IMAGE)
