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
	@set PYTHONDONTWRITEBYTECODE=1 && poetry run python -m unittest discover tests/ -v
else
	@PYTHONDONTWRITEBYTECODE=1 poetry run python3 -m unittest discover tests/ -v
endif

changelog:
	@command -v git-cliff >/dev/null 2>&1 || { \
		echo "Error: git-cliff is not installed."; \
		echo ""; \
		echo "To install git-cliff, visit: https://git-cliff.org/docs/installation"; \
		echo ""; \
		echo "Quick install options:"; \
		echo "  - cargo install git-cliff"; \
		echo "  - brew install git-cliff (macOS)"; \
		echo "  - Or download from: https://github.com/orhun/git-cliff/releases"; \
		exit 1; \
	}
	@git cliff -o CHANGELOG.md
