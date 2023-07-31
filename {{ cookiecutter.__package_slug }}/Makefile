.DEFAULT_GOAL := all
sources = src/{{ cookiecutter.__package_slug }} tests docs/plugins docs

.PHONY: .venv  ## Check that the virtual environment is created
.venv:
	if [ -d ./.venv ]; then echo "Directory exists"; else echo "There is not a venv. Making venv it..." && python -m venv .venv; fi

.PHONY: .pre-commit  ## Check that pre-commit is installed
.pre-commit:
	@pre-commit -V || echo 'Please install pre-commit: https://pre-commit.com/'

.PHONY: install  ## Install the package, dependencies, and pre-commit for local development
install: activate
	pip install --upgrade pip
	pip install -r requirements-dev.txt
	pre-commit install --install-hooks

.PHONY: format  ## Auto-format python source files
format:
	black $(sources)
	ruff --fix $(sources)
	mypy $(sources)

.PHONY: activate  ## Activate python virtual environment
activate: .venv
	source "./.venv/bin/activate"

.PHONY: test  ## Run all tests, skipping the type-checker integration tests
test:
	coverage run -m pytest --durations=10

.PHONY: benchmark  ## Run all benchmarks
benchmark:
	coverage run -m pytest --durations=10 --benchmark-enable tests/benchmarks

.PHONY: testcov  ## Run tests and generate a coverage report, skipping the type-checker integration tests
testcov: test
	@echo "building coverage html"
	@coverage html
	@echo "building coverage lcov"
	@coverage lcov

.PHONY: test-examples  ## Run only the tests from the documentation
test-examples:
	@echo "running examples"
	@find docs/examples -type f -name '*.py' | xargs -I'{}' sh -c 'python {} >/dev/null 2>&1 || (echo "{} failed")'

.PHONY: all  ## Run the standard set of checks performed in CI
all: format testcov

.PHONY: clean  ## Clear local caches and build artifacts
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]'`
	rm -f `find . -type f -name '*~'`
	rm -f `find . -type f -name '.*~'`
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf htmlcov
	rm -rf *.egg-info
	rm -f .coverage
	rm -f .coverage.*
	rm -rf build
	rm -rf dist
	rm -rf site
	rm -rf docs/_build
	rm -rf docs/.changelog.md docs/.version.md docs/.tmp_schema_mappings.html
	rm -rf fastapi/test.db
	rm -rf coverage.xml

# TODO: CHANGE FROM MKDOCS TO SPHANIX
.PHONY: docs  ## Generate the docs
docs:
	mkdocs build

.PHONY: help  ## Display this message
help:
	@grep -E \
		'^.PHONY: .*?## .*$$' $(MAKEFILE_LIST) | \
		sort | \
		awk 'BEGIN {FS = ".PHONY: |## "}; {printf "\033[36m%-19s\033[0m %s\n", $$2, $$3}'

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
BUCKET = {{ cookiecutter.s3_bucket }}
PROFILE = {{ cookiecutter.aws_profile }}
PROJECT_NAME = {{ cookiecutter.__package_slug }}


data: activate  ## Make Dataset, it also need the package to be installed: make install
	{{ cookiecutter.__package_slug }} create-dataset

train: activate  ## Train model using the hyperparameters fixed in the config file
	echo "WIP: Not implemented"
	# {{ cookiecutter.__package_slug }} train-model

train-hyperparameters:
	echo "WIP: Not implemented"

predict: activate  ## Predict using the best model on MLFlow
	echo "WIP: Not implemented"

deply: activate
	echo "WIP: Not implemented"

# TODO: fichero de configuracion: 
# tengo que tomar una decision: hydra, pydantic, dotenv, basic:
#  creo que la que mas me gusta es la de pydantuc + dotevn + yaml
# TODO: pytest arguments on pyproject
# TODO: los procesos de train predict deploy hyperparameters
# TODO: Tambien es interesante definir un sitio para nuevas metricas.
# TODO: documentation