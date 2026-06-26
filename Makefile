.PHONY: help install lint fmt test validate validate-all clean hooks update-hooks

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := uv pip

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

install: $(VENV)/bin/activate ## Create venv and install dependencies
$(VENV)/bin/activate: requirements.txt
	uv venv $(VENV)
	$(PIP) install -r requirements.txt
	@touch $(VENV)/bin/activate

hooks: install ## Install pre-commit git hooks
	$(VENV)/bin/pre-commit install

lint: install ## Run yamllint on device and module types
	$(VENV)/bin/yamllint --format parsable --strict device-types/ module-types/

fmt: install ## Format YAML files with yamlfmt
	$(VENV)/bin/pre-commit run yamlfmt --all-files

test: install ## Run pytest (only changed files vs upstream)
	$(VENV)/bin/pytest --tb=short -v

validate: install ## Run all pre-commit hooks on all files
	$(VENV)/bin/pre-commit run --all-files

validate-all: install ## Run pytest on ALL files (full validation)
	$(VENV)/bin/pytest --tb=short -v --all

clean: ## Remove venv, caches, and generated files
	rm -rf $(VENV) .pytest_cache tests/__pycache__

update-hooks: install ## Update pre-commit hooks to latest versions
	$(VENV)/bin/pre-commit autoupdate
