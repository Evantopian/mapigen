
.PHONY: lint populate populate-force populate-debug validate clean

lint:
	ruff check .

# Default populate uses the cache for efficiency
populate:
	python3 tools/populate_data.py --cache

# Force a clean rebuild without the cache
populate-force:
	python3 tools/populate_data.py

populate-debug:
	python3 tools/populate_data.py --keep-raw-specs --no-compress

validate:
	python3 tools/validate_data.py

clean:
	rm -rf src/mapigen/data
