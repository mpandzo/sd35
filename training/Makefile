SHELL := /bin/bash

default:
	@echo "Check targets!"

init:
	python3 -m venv .venv

activate:
	. .venv/bin/activate

freeze:
	make activate && pip freeze > requirements.txt

install:
	make activate && pip install -r requirements.txt && accelerate config

train:
	make activate && ./train.sh