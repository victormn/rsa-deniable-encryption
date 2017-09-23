# Deniable Encryption Makefile

init:
	pip install -r requirements.txt

test:
	py.test tests

coverage:
	py.test --cov=deniable --cov-report=term --cov-report=html

.PHONY: init test