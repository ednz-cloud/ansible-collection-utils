## v0.10.1 (2025-12-22)

### Fix

- **roles/install_docker**: remove support for zsh shell completion

## v0.10.0 (2025-11-15)

### Feat

- **roles**: add dns role

### Fix

- **roles/manage_netplan**: remove deprecated ansible_managed variable
- **roles/docker_systemd_service**: remove deprecated ansible_managed variable
- **roles**: adjust tag trimming in install_docker role for new tagging convention

## v0.9.0 (2025-09-04)

### Feat

- **modules**: add to_ini_list filter plugin

## v0.8.1 (2025-09-01)

### Fix

- **roles**: remove dependencies on deprecated roles

## v0.8.0 (2025-08-31)

### Feat

- **roles/motd**: add motd role

## v0.7.2 (2025-08-30)

### Fix

- **roles/docker_systemd_service**: adjust conditional for extra_files feature

## v0.7.1 (2025-08-20)

### Fix

- **roles/manage_apt_packages**: adjust conditional on packages install

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
