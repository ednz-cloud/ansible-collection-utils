import pytest


@pytest.mark.parametrize(
    "options, expected",
    [
        # Empty dict produces empty string
        ({}, ""),
        # Single scalar value
        ({"Restart": "always"}, "Restart=always"),
        # Multiple scalar values are sorted by key
        (
            {"RestartSec": "10s", "Restart": "always"},
            "Restart=always\nRestartSec=10s",
        ),
        # List value produces repeated directives
        (
            {"WantedBy": ["multi-user.target", "default.target"]},
            "WantedBy=multi-user.target\nWantedBy=default.target",
        ),
        # Single-item list
        (
            {"WantedBy": ["multi-user.target"]},
            "WantedBy=multi-user.target",
        ),
        # Mixed scalar and list values
        (
            {
                "Restart": "always",
                "Volume": ["/data:/data:z", "/config:/config:ro"],
            },
            "Restart=always\nVolume=/data:/data:z\nVolume=/config:/config:ro",
        ),
        # Typical [Container] section defaults
        (
            {
                "ContainerName": "my_service",
                "EnvironmentFile": "/etc/default/my_service",
                "Image": "nginx:latest",
            },
            "ContainerName=my_service\nEnvironmentFile=/etc/default/my_service\nImage=nginx:latest",
        ),
        # Typical [Install] section
        (
            {"WantedBy": ["multi-user.target"]},
            "WantedBy=multi-user.target",
        ),
        # Integer value
        ({"TimeoutStartSec": 30}, "TimeoutStartSec=30"),
        # Multiple repeated directives alongside scalars
        (
            {
                "Image": "nginx:latest",
                "PublishPort": ["8080:80", "8443:443"],
                "ContainerName": "web",
            },
            "ContainerName=web\nImage=nginx:latest\nPublishPort=8080:80\nPublishPort=8443:443",
        ),
    ],
    ids=[
        "empty_dict",
        "single_scalar",
        "multiple_scalars_sorted",
        "list_value_repeated_directives",
        "single_item_list",
        "mixed_scalar_and_list",
        "container_section_defaults",
        "install_section",
        "integer_value",
        "multiple_repeated_with_scalars",
    ],
)
def test_to_systemd_section_variants(_to_systemd_section, options, expected):
    result = _to_systemd_section(options)
    assert result == expected
