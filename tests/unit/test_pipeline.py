from __future__ import annotations
from pathlib import Path

from mapigen.tools import pipeline


def test_process_spec_file_failure(tmp_path: Path):
    """Tests that process_spec_file handles a corrupted spec file gracefully."""
    # Create a dummy structure
    spec_path = tmp_path / "provider" / "source" / "api" / "api.openapi.json.zst"
    spec_path.parent.mkdir(parents=True)
    spec_path.write_text("corrupted data")

    result = pipeline.process_spec_file(spec_path)
    assert result["status"] == "failure"


def test_create_balanced_batches(tmp_path: Path):
    """Tests that create_balanced_batches creates balanced batches."""
    # Create dummy files with sizes
    sizes = [1000, 100, 900, 200, 800, 300, 700, 400, 600, 500]
    spec_paths = []
    for i, size in enumerate(sizes):
        p = tmp_path / f"spec_{i}.zst"
        p.write_bytes(b"a" * size)
        spec_paths.append(p)

    batches = pipeline.create_balanced_batches(spec_paths, 3)

    # Check that the number of batches is correct
    assert len(batches) == 3

    # Check that the batches are roughly balanced
    batch_sizes = [sum(p.stat().st_size for p in batch) for batch in batches]
    assert max(batch_sizes) - min(batch_sizes) < 1000