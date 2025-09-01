from __future__ import annotations
import pytest
from pathlib import Path

from mapigen.tools import utils
from .. import helpers


def test_load_spec_unsupported_file_type(tmp_path: Path):
    """Tests that load_spec raises a ValueError for an unsupported file type."""
    unsupported_file = helpers.create_unsupported_file(tmp_path, "unsupported")
    with pytest.raises(ValueError):
        utils.load_spec(unsupported_file)


def test_resolve_ref_broken_ref():
    """Tests that _resolve_ref handles a broken $ref gracefully."""
    spec = helpers.create_mock_spec_with_broken_ref()
    broken_ref = "#/components/parameters/param2"
    assert utils._resolve_ref(spec, broken_ref) == {}
