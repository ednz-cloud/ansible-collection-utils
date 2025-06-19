import pytest


@pytest.mark.parametrize(
    "results, item, expected",
    [
        ([{"item": "foo", "changed": True}], "foo", True),
        ([{"item": "foo", "changed": False}], "foo", False),
        ([{"item": "bar", "changed": True}], "foo", False),
        (
            [
                {"item": "foo", "changed": False},
                {"item": "bar", "changed": True},
                {"item": "baz", "changed": False},
            ],
            "bar",
            True,
        ),
        (
            [
                {"item": "foo", "changed": False},
                {"item": "bar", "changed": False},
            ],
            "bar",
            False,
        ),
        ([{"item": "foo"}], "foo", False),
        ([], "foo", False),
        (
            [
                {"item": "foo", "changed": True},
                {"item": "foo", "changed": False},
            ],
            "foo",
            True,
        ),
        (
            [
                {"item": "foo", "changed": False},
                {"item": "foo", "changed": False},
            ],
            "foo",
            False,
        ),
    ],
)
def test_item_changed_in_list_variants(_item_changed_in_list, results, item, expected):
    assert _item_changed_in_list(results, item) == expected


def test_item_changed_in_list_invalid_results(_item_changed_in_list):
    with pytest.raises(ValueError):
        _item_changed_in_list("not a list", "foo")


def test_item_changed_in_list_invalid_item(_item_changed_in_list):
    with pytest.raises(ValueError):
        _item_changed_in_list([], 123)


def test_item_changed_in_list_result_dict_missing_item(_item_changed_in_list):
    results = [{"not_item": "foo", "changed": True}]
    assert _item_changed_in_list(results, "foo") is False
