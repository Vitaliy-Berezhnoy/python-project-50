pytest:
		uv run pytest -s --cov --cov-report=term-missing

install:
	uv sync

run:
	uv run gendiff tests/test_data/1/file1.json tests/test_data/1/file2.json

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml

lint:
	uv run ruff check

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build