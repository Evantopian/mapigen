
.PHONY: lint populate populate-debug validate clean

lint:
	ruff check .

populate:
	python3 tools/populate_data.py

populate-debug:
	python3 tools/populate_data.py --keep-raw-specs --no-compress

validate:
	python3 tools/validate_data.py

clean:
	rm -rf src/mapigen/data
