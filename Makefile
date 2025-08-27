
.PHONY: lint populate populate-force populate-debug validate clean

lint:
	ruff check .

# Default populate uses the cache for efficiency
populate:
	python3 -m tools.populate_data --cache

# Force a clean rebuild without the cache
populate-force:
	python3 -m tools.populate_data

populate-debug:
	python3 -m tools.populate_data --keep-raw-specs --no-compress

validate:
	python3 -m tools.validate_data

clean:
	rm -rf src/mapigen/data
