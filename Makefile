NAME=tedmiston/wtf-covid-19-ohio
TAG=latest
IMAGE=$(NAME):$(TAG)

# -- build --

.PHONY: build
build:
	docker build --target=prod --tag=$(IMAGE) .

.PHONY: build-test
build-test:
	docker build --target=test --tag=$(IMAGE)-test .

# -- run --

.PHONY: run
run:
	docker run --rm $(IMAGE)

# -- test --

.PHONY: test
test:
	poetry run coverage run --source=app --omit=tests/*.py -m pytest

.PHONY: test-docker
test-docker: build-test
	docker run --rm $(IMAGE)-test

# -- mypy --

.PHONY: mypy
mypy:
	poetry run mypy --strict --ignore-missing-imports . tests/

# -- coverage --

.PHONY: coverage
coverage:
	poetry run coverage report

.PHONY: coverage-html
coverage-html:
	poetry run coverage html

.PHONY: coverage-html-show
coverage-html-show: coverage-html
	cd htmlcov/ && open http://localhost:8000 && poetry run python -m http.server

# -- format --

.PHONY: format-check
format-check:
	poetry run black --check .

.PHONY: format-dry-run
format-dry-run:
	poetry run black --diff .

.PHONY: format
format:
	poetry run black .

# -- misc --

.PHONY: push
push:
	./ci/push.sh $(IMAGE)

cache-clear:
	rm "${HOME}/.wtf-coronavirus-ohio/cache.sqlite"
