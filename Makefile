define USAGE
Super awesome hand-crafted build system ⚙️

Commands:
	setup     Install dependencies, dev included
	lock      Generate requirements.txt
	test      Run tests
	lint      Run linting tests
	run       Run docker image with --rm flag but mounted dirs.
	release   Publish docker image based on some variables
	docker    Build the docker image
	tag    	  Make a git tab using poetry information

endef

export USAGE
.EXPORT_ALL_VARIABLES:
VERSION := $(shell git describe --tags)
BUILD := $(shell git rev-parse --short HEAD)
PROJECTNAME := $(shell basename "$(PWD)")
PACKAGE_DIR = $(shell basename "$(PWD)")
DOCKERID = $(shell echo "nuxion")
REGISTRY := registry.nyc1.algorinfo
DATASRV := 10.2.2.2
tarfile := dataproc-${VERSION}.tar.gz
filename := dataproc-${VERSION}

help:
	@echo "$$USAGE"

.PHONY: startenv
startenv:
	poetry shell
	docker-compose start
	alembic upgrade head

lock:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

prepare: lock
	poetry build
	echo ${PWD}
	tar xvfz dist/${tarfile} -C dist/
	cp dist/${filename}/setup.py .
	rm -Rf dist/


.PHONY: lint
lint:
	echo "Running pylint...\n"
	pylint --disable=R,C,W $(PACKAGE_DIR)
	# echo "Running isort...\n"
	# isort --check $(PACKAGE_DIR)
	# echo "Running mypy...\n"
	# mypy $(PACKAGE_DIR)

.PHONY: test
test:
	PYTHONPATH=$(PWD) pytest tests/

.PHONY: install
install:
	poetry install --dev

.PHONY: docker-run
docker-run:
	docker run --rm -p 127.0.0.1:8100:8000 -p 127.0.0.1:8110:8001 ${DOCKERID}/${PROJECTNAME}

.PHONY: runserver
runserver:
	python3 manage.py runserver

.PHONY: run
run:
	# run django and vite server together 
	python3 scripts/run.py

.PHONY: docker
docker:
	docker build -t ${DOCKERID}/${PROJECTNAME} .

.PHONY: docker-local
docker-local:
	docker build -t ${DOCKERID}/${PROJECTNAME} .
	docker tag ${DOCKERID}/${PROJECTNAME} ${DOCKERID}/${PROJECTNAME}:$(VERSION)

.PHONY: release
release:
	docker tag ${DOCKERID}/${PROJECTNAME} ${REGISTRY}/${DOCKERID}/${PROJECTNAME}:$(VERSION)
	docker push ${REGISTRY}/${DOCKERID}/${PROJECTNAME}:$(VERSION)

.PHONY: publish
publish:
	python3 scripts/publish.py

.PHONY: docker-env
docker-env:
	# docker run --rm -it --network host --env-file=.env.docker -v ${PWD}:/app ${REGISTRY}/${DOCKERID}/${PROJECTNAME}:${VERSION} bash
	docker run --rm -it --network host --env-file=.env.docker  -v ${PWD}:/app ${DOCKERID}/${PROJECTNAME} bash

.PHONY: tag
tag:
	# https://git-scm.com/docs/pretty-formats/2.20.0
	#poetry version prealese
	git tag -a $(shell poetry version --short) -m "$(shell git log -1 --pretty=%s | head -n 1)"
