.PHONY: build format run

NAME=tedmiston/wtf-covid-19-ohio
TAG=latest
IMAGE=$(NAME):$(TAG)

build:
	@DOCKER_BUILDKIT=1 docker build --tag=$(IMAGE) .

run:
	@docker run $(IMAGE)

format:
	@black .

push:
	@docker push $(IMAGE)
