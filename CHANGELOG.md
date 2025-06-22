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
