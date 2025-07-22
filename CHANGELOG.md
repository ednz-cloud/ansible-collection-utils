## v0.7.0 (2025-07-22)

### Feat

- **roles/docker_systemd_service**: add extra_file option to track config files for container services
- **roles/docker_systemd_service**: add option to uninstall a service

## v0.6.0 (2025-07-09)

### Feat

- **roles**: add manage_pip_packages roles

## v0.5.0 (2025-06-27)

### Feat

- **roles**: add manage_apt_packages roles

### Fix

- **roles**: add documentation for manage_apt_packages role

## v0.4.0 (2025-06-24)

### Feat

- **roles**: add manage_repositories role

## v0.3.0 (2025-06-22)

### Feat

- **roles**: add manage_netplan role

## v0.2.0 (2025-06-22)

### Feat

- **roles**: add install_docker role
- **plugins**: add item_changed_in_list filter plugin

### Fix

- add pre-commit docsible script

## v0.1.0 (2025-06-18)

### Feat

- **roles**: add docker_system_service role

### Fix

- **roles**: remove install wantedby docker.service for docker_systemd_service unit file template
- adjust default ExecStart to account for empty flag list
