<!-- DOCSIBLE START -->

# 📃 Role overview

## install_docker



Description: Install and configure docker for debian-based distros.


| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 19/06/2025 |








### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [install_docker_version](defaults/main.yml#L10)   | str | `latest` |    false  |  Docker version to install |
| [install_docker_start_service](defaults/main.yml#L17)   | bool | `True` |    false  |  Start Docker service |
| [install_docker_data_dir](defaults/main.yml#L24)   | str | `/var/lib/docker` |    false  |  Docker data directory |
| [install_docker_users](defaults/main.yml#L31)   | list | `[]` |    false  |  Additional Docker group users |
| [install_docker_daemon_options](defaults/main.yml#L38)   | dict | `{}` |    false  |  Docker daemon options |
| [install_docker_python_packages](defaults/main.yml#L45)   | bool | `False` |    false  |  Install Docker Python packages |
| [install_docker_compose](defaults/main.yml#L52)   | bool | `False` |    false  |  Install Docker Compose |
| [install_docker_compose_version](defaults/main.yml#L59)   | str | `latest` |    false  |  Docker Compose version |
| [install_docker_install_completion](defaults/main.yml#L66)   | bool | `True` |    false  |  Install shell completions |
| [install_docker_completion_shell](defaults/main.yml#L73)   | str | `bash` |    false  |  Shell type for completion |
<details>
<summary><b>🖇️ Full descriptions for vars in defaults/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>install_docker_version</b></td><td>Specifies the version of Docker to install.<br>
Use 'latest' to always get the most recent release from Docker's GitHub repository.<br>
You can also specify a version tag (e.g., '24.0.7').<br></td></tr>
<tr><td><b>install_docker_start_service</b></td><td>Determines whether the Docker service should be started after installation.<br>
Set to true to start the service automatically.<br></td></tr>
<tr><td><b>install_docker_data_dir</b></td><td>Sets the root directory used by Docker to store container data, images, and volumes.<br>
Changing this may require updating the daemon configuration and moving existing data.<br></td></tr>
<tr><td><b>install_docker_users</b></td><td>List of system users to be added to the 'docker' group.<br>
This allows the specified users to run Docker commands without sudo.<br></td></tr>
<tr><td><b>install_docker_daemon_options</b></td><td>Dictionary of custom options to include in the Docker daemon configuration (daemon.json).<br>
Common options include log-driver, storage-driver, and insecure registries.<br></td></tr>
<tr><td><b>install_docker_python_packages</b></td><td>Whether to install Python packages required for Ansible Docker modules (e.g., docker-py).<br>
Set to true if you plan to manage containers via Ansible tasks.<br></td></tr>
<tr><td><b>install_docker_compose</b></td><td>Determines whether Docker Compose should be installed.<br>
If true, the version specified in install_docker_compose_version will be downloaded from GitHub.<br></td></tr>
<tr><td><b>install_docker_compose_version</b></td><td>Specifies the version of Docker Compose to install from GitHub releases.<br>
Use 'latest' to install the most recent stable version, or specify a version tag (e.g., 'v2.27.0').<br></td></tr>
<tr><td><b>install_docker_install_completion</b></td><td>Controls whether Docker CLI autocompletion scripts should be installed.<br>
Enhances shell usability for Docker commands.<br></td></tr>
<tr><td><b>install_docker_completion_shell</b></td><td>Defines the shell type (e.g., bash) for which Docker completion scripts should be installed.<br>
Currently, the only supported shell is bash.<br></td></tr>
</table>
<br>
</details>


### Vars

**These are variables with higher priority**
#### File: vars/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [install_docker_binary_path](vars/main.yml#L7)   | str | `/usr/local/bin` |    false  |  Docker binary installation path |
| [install_docker_compose_path](vars/main.yml#L12)   | str | `{{ install_docker_binary_path }}/docker-compose` |    false  |  Docker Compose binary path |
| [install_docker_user](vars/main.yml#L17)   | str | `root` |    false  |  Owner user for Docker files |
| [install_docker_group](vars/main.yml#L22)   | str | `docker` |    false  |  Docker system group |
| [install_docker_daemon_dir](vars/main.yml#L27)   | str | `/etc/docker` |    false  |  Docker daemon config directory |
| [install_docker_service_list](vars/main.yml#L32)   | list | `[]` |    false  |  Docker-related system services |
| [install_docker_service_list.**0**](vars/main.yml#L33)   | str | `containerd` |    None  |  None |
| [install_docker_service_list.**1**](vars/main.yml#L34)   | str | `docker` |    None  |  None |
| [install_docker_socket_list](vars/main.yml#L39)   | list | `[]` |    false  |  Docker-related Unix sockets |
| [install_docker_socket_list.**0**](vars/main.yml#L39)   | str | `docker` |    false  |  Docker-related Unix sockets |
| [install_docker_architecture_map](vars/main.yml#L45)   | dict | `{}` |    false  |  Docker architecture mapping |
| [install_docker_architecture_map.**armv7l**](vars/main.yml#L46)   | str | `armhf` |    None  |  None |
| [install_docker_architecture_map.**armv6l**](vars/main.yml#L47)   | str | `armhf` |    None  |  None |
| [install_docker_python_packages_list](vars/main.yml#L52)   | list | `[]` |    false  |  Python packages for Docker support |
| [install_docker_python_packages_list.**0**](vars/main.yml#L53)   | dict | `{}` |    None  |  None |
| [install_docker_python_packages_list.0.**name**](vars/main.yml#L53)   | str | `python3-docker` |    None  |  None |
| [install_docker_python_packages_list.0.**version**](vars/main.yml#L54)   | str | `latest` |    None  |  None |
| [install_docker_python_packages_list.0.**state**](vars/main.yml#L55)   | str | `present` |    None  |  None |
| [install_docker_sysctl_entries](vars/main.yml#L60)   | dict | `{}` |    false  |  Docker-related sysctl entries |
| [install_docker_sysctl_entries.net.bridge.**bridge-nf-call-iptables**](vars/main.yml#L61)   | int | `1` |    None  |  None |
| [install_docker_sysctl_entries.net.bridge.**bridge-nf-call-ip6tables**](vars/main.yml#L62)   | int | `1` |    None  |  None |
| [install_docker_modprobe_modules](vars/main.yml#L67)   | list | `[]` |    false  |  Kernel modules for Docker |
| [install_docker_modprobe_modules.**0**](vars/main.yml#L68)   | str | `br_netfilter` |    None  |  None |
| [install_docker_github_api](vars/main.yml#L73)   | str | `https://api.github.com/repos` |    false  |  GitHub API base URL |
| [install_docker_github_url](vars/main.yml#L78)   | str | `https://github.com` |    false  |  GitHub base URL |
| [install_docker_github_project](vars/main.yml#L83)   | str | `moby/moby` |    false  |  GitHub project for Docker |
| [install_docker_repository_url](vars/main.yml#L88)   | str | `https://download.docker.com/linux/static/stable/{{ install_docker_architecture_map[ansible_architecture]¦default(ansible_architecture) }}` |    false  |  Docker release repository URL |
| [install_docker_compose_github_project](vars/main.yml#L93)   | str | `docker/compose` |    false  |  GitHub project for Docker Compose |
<details>
<summary><b>🖇️ Full Descriptions for vars in vars/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>install_docker_binary_path</b></td><td>Filesystem path where Docker binaries will be installed</td></tr>
<tr><td><b>install_docker_compose_path</b></td><td>Path where the Docker Compose binary will be installed</td></tr>
<tr><td><b>install_docker_user</b></td><td>System user that owns Docker-related files and directories</td></tr>
<tr><td><b>install_docker_group</b></td><td>Group used for granting access to the Docker socket</td></tr>
<tr><td><b>install_docker_daemon_dir</b></td><td>Filesystem path to Docker's daemon configuration files</td></tr>
<tr><td><b>install_docker_service_list</b></td><td>List of system services managed by the role during install</td></tr>
<tr><td><b>install_docker_socket_list</b></td><td>List of Docker socket names to check/manage</td></tr>
<tr><td><b>install_docker_socket_list.0</b></td><td>List of Docker socket names to check/manage</td></tr>
<tr><td><b>install_docker_architecture_map</b></td><td>Maps Ansible system architecture names to GitHub Docker release architecture names</td></tr>
<tr><td><b>install_docker_python_packages_list</b></td><td>List of Python packages required for Docker Ansible modules</td></tr>
<tr><td><b>install_docker_sysctl_entries</b></td><td>Kernel sysctl parameters required for Docker networking</td></tr>
<tr><td><b>install_docker_modprobe_modules</b></td><td>List of kernel modules to load for Docker functionality</td></tr>
<tr><td><b>install_docker_github_api</b></td><td>Base URL for GitHub API used to fetch Docker release data</td></tr>
<tr><td><b>install_docker_github_url</b></td><td>Base URL for GitHub used to construct download links</td></tr>
<tr><td><b>install_docker_github_project</b></td><td>GitHub repository for Docker Engine releases</td></tr>
<tr><td><b>install_docker_repository_url</b></td><td>URL to fetch Docker static binaries based on system architecture</td></tr>
<tr><td><b>install_docker_compose_github_project</b></td><td>GitHub repository for Docker Compose releases</td></tr>
</table>
<br>
</details>


### Tasks


#### File: tasks/configure.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Docker ¦ Add specified users to group {{ install_docker_group }} | ansible.builtin.user | False |
| Docker ¦ Copy daemon.json template | ansible.builtin.template | False |
| Docker ¦ Set reload-check & restart-check variable | ansible.builtin.set_fact | True |
| Docker ¦ Ensure modprobe modules are loaded | community.general.modprobe | False |
| Docker ¦ Ensure sysctl options are proprerly set | ansible.posix.sysctl | False |
| Docker ¦ Set restart-check variable | ansible.builtin.set_fact | True |
| Docker ¦ Install completion for bash | block | True |
| Docker ¦ Get docker completion | ansible.builtin.command | False |
| Docker ¦ Ensure /etc/bash_completion.d directory exists | ansible.builtin.file | False |
| Docker ¦ Copy bash completion | ansible.builtin.copy | False |

#### File: tasks/install.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Docker ¦ Get latest release of docker | block | True |
| Docker ¦ Get latest docker release from github api | ansible.builtin.uri | False |
| Docker ¦ Set wanted docker version to latest tag | ansible.builtin.set_fact | False |
| Docker ¦ Set wanted docker version to {{ install_docker_version }} | ansible.builtin.set_fact | True |
| Docker ¦ Get current docker version | block | False |
| Docker ¦ Stat docker version file | ansible.builtin.stat | False |
| Docker ¦ Get current docker version | ansible.builtin.slurp | True |
| Docker ¦ Download and install docker binaries | block | True |
| Docker ¦ Set docker package name to download | ansible.builtin.set_fact | False |
| Docker ¦ Download docker binary archive | ansible.builtin.get_url | False |
| Docker ¦ Create temporary directory for archive decompression | ansible.builtin.file | False |
| Docker ¦ Unpack docker archive | ansible.builtin.unarchive | False |
| Docker ¦ Get list of binaries | ansible.builtin.find | False |
| Docker ¦ Copy docker binaries to {{ install_docker_binary_path }} | ansible.builtin.copy | False |
| Docker ¦ Update docker version file | ansible.builtin.copy | False |
| Docker ¦ Set restart-check variable | ansible.builtin.set_fact | False |
| Docker ¦ Cleanup temporary directory | ansible.builtin.file | False |
| Docker ¦ Copy systemd service files for docker | ansible.builtin.template | False |
| Docker ¦ Copy systemd socket files for docker | ansible.builtin.template | False |
| Docker ¦ Set reload-check & restart-check variable | ansible.builtin.set_fact | True |

#### File: tasks/install_compose.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Docker ¦ Get release for compose:{{ install_docker_compose_version }} | ansible.builtin.uri | False |
| Docker ¦ Check current compose version | ansible.builtin.command | False |
| Docker ¦ Set facts for wanted compose release | ansible.builtin.set_fact | True |
| Docker ¦ Set facts for current compose release | ansible.builtin.set_fact | True |
| Docker ¦ Remove old compose binary if different | ansible.builtin.file | True |
| Docker ¦ Download and install compose:{{ install_docker_compose_version }} | ansible.builtin.get_url | True |

#### File: tasks/install_python_docker.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Install docker packages | ansible.builtin.include_role | False |

#### File: tasks/main.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Docker ¦ Set reload-check & restart-check variable | ansible.builtin.set_fact | False |
| Import prerequisites.yml | ansible.builtin.include_tasks | False |
| Import install.yml | ansible.builtin.include_tasks | False |
| Import install_compose.yml | ansible.builtin.include_tasks | True |
| Import install_python_docker.yml | ansible.builtin.include_tasks | True |
| Import configure.yml | ansible.builtin.include_tasks | False |
| Docker ¦ Enable sockets: {{ install_docker_socket_list }} | ansible.builtin.service | False |
| Docker ¦ Enable services: {{ install_docker_service_list }} | ansible.builtin.service | False |
| Docker ¦ Reload systemd daemon | ansible.builtin.systemd | True |
| Docker ¦ Reload services: docker | ansible.builtin.service | True |
| Docker ¦ Start services: {{ install_docker_service_list }} | ansible.builtin.service | True |

#### File: tasks/prerequisites.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Create group {{ install_docker_group }} | ansible.builtin.group | False |
| Create directory {{ install_docker_daemon_dir }} | ansible.builtin.file | False |
| Create directory {{ install_docker_data_dir }} | ansible.builtin.file | False |







## Author Information
Bertrand Lanson

#### License

license (BSD, MIT)

#### Minimum Ansible Version

2.10

#### Platforms

- **Ubuntu**: ['jammy', 'noble']
- **Debian**: ['bookworm', 'trixie']


#### Dependencies

No dependencies specified.
<!-- DOCSIBLE END -->
