import pytest
from ansible_collections.ednz_cloud.utils.plugins.filter import (
    item_changed_in_list,
    to_cli_flags,
    to_systemd_section,
)


@pytest.fixture
def _to_cli_flags():
    return to_cli_flags.FilterModule().filters()["to_cli_flags"]


@pytest.fixture
def _item_changed_in_list():
    return item_changed_in_list.FilterModule().filters()["item_changed_in_list"]


@pytest.fixture
def _to_systemd_section():
    return to_systemd_section.FilterModule().filters()["to_systemd_section"]
