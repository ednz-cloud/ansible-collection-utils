import pytest


@pytest.mark.parametrize(
    "flags, multiline, trailing_backslash, expected",
    [
        ([], False, False, ""),
        (None, False, False, ""),
        (["rm"], False, False, "--rm"),
        (["rm"], True, False, "--rm"),
        (["rm"], True, True, "--rm \\"),
        (["rm", "privileged"], False, False, "--rm --privileged"),
        (["rm", "privileged"], True, False, "--rm \\\n--privileged"),
        (["rm", "privileged"], True, True, "--rm \\\n--privileged \\"),
        ([{"rm": True}, {"detach": False}], False, False, "--rm"),
        ([{"rm": False}, {"interactive": True}], False, False, "--interactive"),
        ([{"name": "my_container"}], False, False, '--name "my_container"'),
        ([{"name": "my_container"}], True, True, '--name "my_container" \\'),
        (
            [{"cap-add": ["SYS_ADMIN", "NET_ADMIN"]}],
            False,
            False,
            '--cap-add "SYS_ADMIN" --cap-add "NET_ADMIN"',
        ),
        (
            [{"cap-add": ["SYS_ADMIN", "NET_ADMIN"]}],
            True,
            False,
            '--cap-add "SYS_ADMIN" \\\n--cap-add "NET_ADMIN"',
        ),
        (
            [{"cap-add": ["SYS_ADMIN", "NET_ADMIN"]}],
            True,
            True,
            '--cap-add "SYS_ADMIN" \\\n--cap-add "NET_ADMIN" \\',
        ),
        (
            [{"env": "PROD"}, {"cap-add": ["SYS_ADMIN"]}, "rm"],
            False,
            False,
            '--env "PROD" --cap-add "SYS_ADMIN" --rm',
        ),
        (
            [{"env": "PROD"}, {"cap-add": ["SYS_ADMIN"]}, "rm"],
            True,
            False,
            '--env "PROD" \\\n--cap-add "SYS_ADMIN" \\\n--rm',
        ),
        ([{"log-driver": None}, "rm"], False, False, "--rm"),
        (
            [{"cap-add": ["NET_ADMIN"]}],
            True,
            False,
            '--cap-add "NET_ADMIN"',
        ),
    ],
    ids=[
        "empty_list",
        "none_input",
        "single_string_flag",
        "single_string_flag_multiline",
        "single_string_flag_multiline_trailing_backslash",
        "multiple_string_flags",
        "multiple_string_flags_multiline",
        "multiple_string_flags_multiline_trailing_backslash",
        "bool_true_and_false_dict_flags",
        "bool_false_and_true_dict_flags",
        "string_value_dict_flag",
        "string_value_dict_flag_multiline_trailing_backslash",
        "list_value_dict_flag",
        "list_value_dict_flag_multiline",
        "list_value_dict_flag_multiline_trailing_backslash",
        "mixed_flags",
        "mixed_flags_multiline",
        "none_value_dict_flag_skipped",
        "single_item_list_multiline",
    ],
)
def test_to_cli_flags_variants(
    _to_cli_flags, flags, multiline, trailing_backslash, expected
):
    result = _to_cli_flags(flags, multiline, trailing_backslash)
    assert result == expected
