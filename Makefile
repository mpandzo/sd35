SHELL := /bin/bash

default:
	@echo "Check targets!"

init:
	python -m venv .venv

activate:
	. .venv/bin/activate

freeze:
	make activate && pip freeze > requirements.txt

install:
	make activate && pip install --upgrade gradio && pip install -r requirements.txt

test-sd35:
	make activate && python test-stable-diffusion.py

test-gradio:
	make activate && python test-gradio.py

# pip install sentencepiece python-dotenv protobuf psutil accelerate transformers diffusers torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/torch_stable.html
