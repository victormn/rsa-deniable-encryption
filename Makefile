# Deniable Encryption Makefile

all: init build

init:
	pip3 install -r requirements.txt

build:
	python3 setup.py install

test:
	py.test tests

coverage:
	py.test --cov-config tests/.coveragerc --cov=deniable --cov-report=term --cov-report=html

.PHONY: init test install build