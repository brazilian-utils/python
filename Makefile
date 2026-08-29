install:
	@git config --local core.hooksPath .githooks/
# This must be indented like this, otherwise it will not work on Windows
# see: https://stackoverflow.com/questions/77974076/how-do-i-fix-this-error-when-checking-os-in-makefile
ifneq ($(OS),Windows_NT)
		@chmod -R +x .githooks
endif
	@poetry install

shell:
	@poetry shell

run-python:
	@poetry run python

format:
	@poetry run ruff format .
	@poetry run ruff check --fix .

check:
	@poetry run ruff format --check .
	@poetry run ruff check .

test:
ifeq ($(OS),Windows_NT)
	@set PYTHONDONTWRITEBYTECODE=1 && poetry run pytest
else
	@PYTHONDONTWRITEBYTECODE=1 poetry run pytest
endif
