.PHONY: help lint test test-report populate populate-force populate-debug validate clean clean-openapi show-format show-data


# Variables
PYTHONPATH := src
PYTHON := PYTHONPATH=$(PYTHONPATH) python3
TOOLS := $(PYTHON) -m mapigen.tools

# Default target
help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

lint: ## Run ruff linter

	ruff check .

test: ## Run pytest. Usage: make test t=tests/path/to/test.py
	@if [ -z "$(t)" ]; then \
			echo "Running all tests..."; \
			pytest -s; \
	else \
			echo "Running specified tests: $(t)"; \
			pytest -s $(t); \
	fi


populate: ## Populate using cached data
	$(TOOLS).populate_data --cache

populate-force: ## Force populate without cache
	$(TOOLS).populate_data

populate-debug: ## Populate in debug mode (keep raw specs, no compression)
	$(TOOLS).populate_data --keep-raw-specs --no-compress

validate: ## Validate populated data
	$(TOOLS).validate_data
	$(TOOLS).deep_validate

inspector: ## Run inspector utility
	@$(PYTHON) utils/inspector.py $(filter-out $@,$(MAKECMDGOALS))

show-format: ## Display the standard SDK response format
	@$(PYTHON) utils/show_format.py


show-data: ## Pretty-print a response file. Usage: make show-data tmp/file.json
	@$(PYTHON) utils/show_format.py $(filter-out $@,$(MAKECMDGOALS))

clean: ## Remove all generated data files (utilize and notice files)
	find src/mapigen/data -type f -name "*.utilize.json*" -delete
	find src/mapigen/registry -type f -name "AUTH_NOTICE.md" -delete
	find . -type f -name "services.json" -delete

clean-openapi: ## Remove only OpenAPI artifacts
	find src/mapigen/data -type f -name "*.openapi.*" -delete
