.PHONY: help lint populate populate-force populate-debug validate clean clean-openapi

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

populate: ## Populate using cached data
	$(TOOLS).populate_data --cache

populate-force: ## Force populate without cache
	$(TOOLS).populate_data

populate-debug: ## Populate in debug mode (keep raw specs, no compression)
	$(TOOLS).populate_data --keep-raw-specs --no-compress

validate: ## Validate populated data
	$(TOOLS).validate_data
	$(TOOLS).deep_validate

 
#clean: ## Remove populated data
#	rm -rf src/mapigen/data

clean-openapi: ## Remove only OpenAPI artifacts
	find src/mapigen/data -type f -name "*.openapi.*" -delete
