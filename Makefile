all: fix lint build-dev build-prod up-dev up-prod down-dev down-prod prune

SRC = src/
TESTS = tests/

install:
	poetry install

uninstall:
	rm -rf ./.venv/
	rm poetry.lock

fix:
	poetry run autoflake -r --remove-all-unused-imports --remove-unused-variables --remove-unused-variables --in-place ${SRC}	
	poetry run black ${SRC}
	poetry run isort ${SRC}
	poetry run toml-sort --in-place pyproject.toml

	poetry run autoflake -r --remove-all-unused-imports --remove-unused-variables --remove-unused-variables --in-place ${TESTS}	
	poetry run black ${TESTS}
	poetry run isort ${TESTS}

lint:
	poetry run flake8 --exclude __init__.py ${SRC}
	poetry run mypy ${SRC}	
	poetry run pyright ${SRC}	

test:
	poetry run pytest ${TESTS} -W ignore::DeprecationWarning
	poetry run pytest --cov=${SRC} -W ignore::DeprecationWarning
	

build:
	docker compose --env-file .env build

build-up:
	docker compose --env-file .env up --build

down:
	docker compose --env-file .env down

prune:
	docker container prune -f
	docker volume prune -f