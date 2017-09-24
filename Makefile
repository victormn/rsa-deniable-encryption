# Deniable Encryption Makefile

init:
	pip3 install -r requirements.txt

test:
	py.test tests

coverage:
	py.test --cov-config tests/.coveragerc --cov=deniable --cov-report=term --cov-report=html

install:
	python3 setup.py install

.PHONY: init test install