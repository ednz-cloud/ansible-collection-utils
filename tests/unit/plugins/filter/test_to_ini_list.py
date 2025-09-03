# plugins/filter/test_to_ini_list.py
import pytest
from ansible_collections.ednz_cloud.utils.plugins.filter import to_ini_list


@pytest.fixture
def _to_ini_list():
    return to_ini_list.FilterModule().filters()["to_ini_list"]


@pytest.mark.parametrize(
    "ini_dict, expected",
    [
        # Empty dict → empty list
        ({}, []),
        # Single section, single key
        (
            {"DEFAULT": {"backend": "systemd"}},
            [{"section": "DEFAULT", "option": "backend", "value": "systemd"}],
        ),
        # Single section, multiple keys
        (
            {"DEFAULT": {"backend": "systemd", "username": "openstack"}},
            [
                {"section": "DEFAULT", "option": "backend", "value": "systemd"},
                {"section": "DEFAULT", "option": "username", "value": "openstack"},
            ],
        ),
        # Nested section (dict)
        (
            {"DEFAULT": {"nested": {"suboption": "value"}}},
            [
                {
                    "section": "DEFAULT.nested",
                    "option": "suboption",
                    "value": "value",
                }
            ],
        ),
        # Nested + sibling key
        (
            {"DEFAULT": {"backend": "systemd", "nested": {"suboption": "value"}}},
            [
                {"section": "DEFAULT", "option": "backend", "value": "systemd"},
                {
                    "section": "DEFAULT.nested",
                    "option": "suboption",
                    "value": "value",
                },
            ],
        ),
        # List values
        (
            {"DEFAULT": {"another": ["list", "of", "values"]}},
            [
                {
                    "section": "DEFAULT",
                    "option": "another",
                    "value": "list,of,values",
                }
            ],
        ),
        # Mixed types (str, int, bool, list, dict)
        (
            {
                "DEFAULT": {
                    "backend": "systemd",
                    "retries": 3,
                    "enabled": True,
                    "nested": {"child": ["a", "b"]},
                }
            },
            [
                {"section": "DEFAULT", "option": "backend", "value": "systemd"},
                {"section": "DEFAULT", "option": "retries", "value": 3},
                {"section": "DEFAULT", "option": "enabled", "value": True},
                {
                    "section": "DEFAULT.nested",
                    "option": "child",
                    "value": "a,b",
                },
            ],
        ),
        # Multiple sections
        (
            {
                "DEFAULT": {"backend": "systemd"},
                "database": {"host": "localhost", "port": "3306"},
            },
            [
                {"section": "DEFAULT", "option": "backend", "value": "systemd"},
                {"section": "database", "option": "host", "value": "localhost"},
                {"section": "database", "option": "port", "value": "3306"},
            ],
        ),
    ],
)
def test_to_ini_list_variants(_to_ini_list, ini_dict, expected):
    result = _to_ini_list(ini_dict)
    assert sorted(result, key=lambda x: (x["section"], x["option"])) == sorted(
        expected, key=lambda x: (x["section"], x["option"])
    )
