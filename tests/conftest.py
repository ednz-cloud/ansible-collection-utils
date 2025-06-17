# tests/conftest.py

import pytest
from ansible_collections.ednz_cloud.utils.plugins.filter import to_cli_flags


@pytest.fixture
def _to_cli_flags():
    return to_cli_flags.FilterModule().filters()["to_cli_flags"]
