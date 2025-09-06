.PHONY: help lint test test-report test-populate populate populate-force populate-debug validate clean clean-openapi show-format show-data


# Variables
PYTHONPATH := src
PYTHON := PYTHONPATH=$(PYTHONPATH) python3
TOOLS := $(PYTHON) -m mapigen.tools

# Default target
help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $1, $2}'

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

test-report: ## Run all tests and generate the integration_targets.yaml report
	@echo "Running tests and generating report..."
	@pytest

test-populate: ## Run integration tests after a fresh data population

	@echo "Populating data..."
	@$(TOOLS).populate_data --force-reprocess && \
		echo "Waiting for filesystem..." && sleep 1 && \
		echo "Running integration tests on populated data..." && \
		pytest -s tests/integration/

test-parallel: ## Run tests in parallel using pytest-xdist
	pytest -n auto -sv


populate: ## Populate data, skipping already processed specs. Pass args with ARGS="--arg1 val1"
	$(TOOLS).populate_data $(ARGS)

populate-force: ## Force populate all specs, reprocessing everything
	$(TOOLS).populate_data --force-reprocess

populate-debug: ## Populate in debug mode (no compression on utilize.json files)
	$(TOOLS).populate_data --no-compress-utilize $(ARGS)

validate: ## Run light validation on populated data
	$(TOOLS).validate_data

deep-validate: ## Run deep validation on populated data (slow). Usage: make deep-validate s=service_name
	@if [ -z "$(s)" ]; then \
			echo "Running deep validation on all services..."; \
			$(TOOLS).deep_validate; \
	else \
			echo "Running deep validation on service: $(s)"; \
			$(TOOLS).deep_validate $(s); \
	fi


validate-all: validate deep-validate ## Run all validation checks
	@echo "All validation checks complete."

generate-tests: ## Generate new integration tests for services without one
	@echo "🐍 Generating new integration tests..."
	@$(PYTHON) utils/generate_integration_tests.py

inspector: ## Run inspector utility
	@$(PYTHON) utils/inspector.py $(filter-out $@,$(MAKECMDGOALS))

profile: ## Run cProfile on the populate script and generate a stats file
	@echo "Profiling the populate-force command..."
	PYTHONPATH=src python3 -m cProfile -s cumulative -o populate.prof src/mapigen/tools/populate_data.py --force-reprocess
	@echo "Profiling complete. To view results, run: make view-profile"

view-profile: ## Open the last profiling session in snakeviz
	snakeviz populate.prof

sCRIPT_PATH ?=
FILTER ?= mapigen
ARGS ?=

custom-profile: ## Profile a script. Usage: make custom-profile SCRIPT_PATH=<path> [FILTER=<str>] [ARGS="--arg1 val1"]
	@if [ -z "$(SCRIPT_PATH)" ]; then \
			echo "Error: Please specify a script to profile with SCRIPT_PATH=<script_path>"; \
			exit 1; \
	fi
	@echo "Running custom profiler on $(SCRIPT_PATH) with filter='$(FILTER)' and args='$(ARGS)'..."
	$(PYTHON) utils/profiler.py $(SCRIPT_PATH) --filter $(FILTER) $(ARGS)

test-profile: ## Run pytest with profiling and output stats to console
	@pytest --profile
	@echo ""
	@echo "Profiling complete. For a more detailed, interactive view, run:"
	@echo "snakeviz prof/combined.prof"

show-format: ## Display the standard SDK response format
	@$(PYTHON) utils/show_format.py


show-data: ## Pretty-print a response file. Usage: make show-data tmp/file.json
	@$(PYTHON) utils/show_format.py $(filter-out $@,$(MAKECMDGOALS))

clean: ## Remove all generated data files (utilize and notice files)
	find src/mapigen/data -type f -name "*.utilize.json*" -delete
	find src/mapigen/data -type f -name "*.zst*" -delete
	find src/mapigen/registry -type f -name "AUTH_NOTICE.md" -delete
	find . -type f -name "services.json" -delete

clean-openapi: ## Remove only OpenAPI artifacts
	find src/mapigen/data -type f -name "*.openapi.*" -delete

clean-tests: ## Remove auto-generated integration test files
	@echo "🧹 Cleaning generated test files..."
	@find tests/integration -type f -name "*_generated.py" -delete
	@echo "Done."