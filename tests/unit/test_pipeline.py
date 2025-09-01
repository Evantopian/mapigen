from __future__ import annotations
from pathlib import Path

from mapigen.tools import pipeline


def test_process_single_service_failure(tmp_path: Path):
    """Tests that process_single_service handles a corrupted spec file gracefully."""
    service_name = "corrupted_service"
    service_data_dir = tmp_path / "data" / service_name
    service_data_dir.mkdir(parents=True)
    spec_path = service_data_dir / f"{service_name}.openapi.json.zst"
    spec_path.write_text("corrupted data")

    result = pipeline.process_single_service(service_name, "http://localhost/corrupted.json")
    assert result["status"] == "failure"


def test_create_balanced_batches():
    """Tests that create_balanced_batches creates balanced batches."""
    services = [
        {"name": "service_a", "size": 1000},
        {"name": "service_b", "size": 100},
        {"name": "service_c", "size": 900},
        {"name": "service_d", "size": 200},
        {"name": "service_e", "size": 800},
        {"name": "service_f", "size": 300},
        {"name": "service_g", "size": 700},
        {"name": "service_h", "size": 400},
        {"name": "service_i", "size": 600},
        {"name": "service_j", "size": 500},
    ]

    batches = pipeline.create_balanced_batches(services, 3)

    # Check that the number of batches is correct
    assert len(batches) == 3

    # Check that the batches are roughly balanced
    batch_sizes = [sum(s['size'] for s in batch) for batch in batches]
    assert max(batch_sizes) - min(batch_sizes) < 1000
