# Deniable Encryption Makefile

init:
	pip install -r requirements.txt

test:
	py.test tests

coverage:
	py.test --cov-config tests/.coveragerc --cov=deniable --cov-report=term --cov-report=html

install:
	python setup.py install

.PHONY: init test install