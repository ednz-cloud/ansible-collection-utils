import pytest
from ansible_collections.ednz_cloud.utils.plugins.filter import (
    to_cli_flags,
    item_changed_in_list,
)


@pytest.fixture
def _to_cli_flags():
    return to_cli_flags.FilterModule().filters()["to_cli_flags"]


@pytest.fixture
def _item_changed_in_list():
    return item_changed_in_list.FilterModule().filters()["item_changed_in_list"]
