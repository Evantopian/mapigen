
.PHONY: lint populate populate-force populate-debug validate clean clean-openapi

lint:
	ruff check .

# Default populate uses the cache for efficiency
populate:
	PYTHONPATH=src python3 -m mapigen.tools.populate_data --cache

# Force a clean rebuild without the cache
populate-force:
	PYTHONPATH=src python3 -m mapigen.tools.populate_data

populate-debug:
	PYTHONPATH=src python3 -m mapigen.tools.populate_data --keep-raw-specs --no-compress

validate:
	PYTHONPATH=src python3 -m mapigen.tools.validate_data

clean:
	rm -rf src/mapigen/data

clean-openapi:
	find src/mapigen/data -type f -name "*.openapi.*" -delete
