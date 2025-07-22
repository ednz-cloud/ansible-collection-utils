<!-- DOCSIBLE START -->

# 📃 Role overview

## docker_systemd_service



Description: Create Systemd services for docker containers.


| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 19/06/2025 |








### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [docker_systemd_service_container_name](defaults/main.yml#L9)   | str | `my_service` |    true  |  Docker container name |
| [docker_systemd_service_image](defaults/main.yml#L16)   | NoneType | `None` |    true  |  Docker image to run |
| [docker_systemd_service_container_env](defaults/main.yml#L23)   | dict | `{}` |    false  |  Container environment variables |
| [docker_systemd_service_container_pull_image](defaults/main.yml#L29)   | bool | `True` |    false  |  Pull image before running |
| [docker_systemd_service_container_pull_force_source](defaults/main.yml#L35)   | bool | `True` |    false  |  Force pull from source registry |
| [docker_systemd_service_flags](defaults/main.yml#L42)   | list | `[]` |    false  |  Additional Docker CLI flags |
| [docker_systemd_service_container_cmd](defaults/main.yml#L49)   | list | `[]` |    false  |  Docker command override |
| [docker_systemd_service_name](defaults/main.yml#L56)   | str | `{{ docker_systemd_service_container_name }}_container` |    false  |  Systemd service name |
| [docker_systemd_service_systemd_unit_options](defaults/main.yml#L64)   | dict | `{}` |    false  |  Systemd unit file options |
| [docker_systemd_service_systemd_service_options](defaults/main.yml#L72)   | dict | `{}` |    false  |  Systemd service options |
| [docker_systemd_service_systemd_install_options](defaults/main.yml#L80)   | dict | `{}` |    false  |  Systemd install options |
| [docker_systemd_service_start](defaults/main.yml#L88)   | bool | `True` |    false  |  Start the systemd service |
| [docker_systemd_service_extra_files](defaults/main.yml#L107)   | list | `[]` |    false  |  Extra files to copy |
| [docker_systemd_service_action](defaults/main.yml#L117)   | str | `install` |    false  |  Action to perform |
<details>
<summary><b>🖇️ Full descriptions for vars in defaults/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>docker_systemd_service_container_name</b></td><td>Name of the Docker container to be managed by the systemd service.<br>
Used as the basis for naming the systemd unit file and identifying the container.<br></td></tr>
<tr><td><b>docker_systemd_service_image</b></td><td>Name of the Docker image to use for the container.<br>
This can include a tag (e.g., 'nginx:latest').<br></td></tr>
<tr><td><b>docker_systemd_service_container_env</b></td><td>Dictionary of environment variables to pass into the container.<br>
Keys are variable names and values are strings or Jinja2 expressions.<br></td></tr>
<tr><td><b>docker_systemd_service_container_pull_image</b></td><td>If true, pulls the latest version of the Docker image before starting the container.<br></td></tr>
<tr><td><b>docker_systemd_service_container_pull_force_source</b></td><td>If true, forces a fresh image pull even if a local image with the same tag exists.<br></td></tr>
<tr><td><b>docker_systemd_service_flags</b></td><td>List of extra flags to pass to the Docker CLI when starting the container.<br>
Useful for custom networking, volume mounts, or runtime options.<br></td></tr>
<tr><td><b>docker_systemd_service_container_cmd</b></td><td>List of arguments to override the default container CMD.<br>
Useful if you want to change the startup behavior of the image.<br></td></tr>
<tr><td><b>docker_systemd_service_name</b></td><td>Name of the systemd service unit that wraps the Docker container.<br>
Defaults to the container name with '_container' suffix.<br></td></tr>
<tr><td><b>docker_systemd_service_systemd_unit_options</b></td><td>Dictionary of raw unit file entries to include in the generated systemd unit.<br>
These settings go under the [Unit] section.<br>
These are merged with the default options defined in docker_systemd_service_systemd_unit_options_default.<br></td></tr>
<tr><td><b>docker_systemd_service_systemd_service_options</b></td><td>Dictionary of raw service options to include under the [Service] section in systemd.<br>
Can include options like Restart=always, TimeoutStartSec, etc.<br>
These are merged with the default options defined in docker_systemd_service_systemd_service_options_default.<br></td></tr>
<tr><td><b>docker_systemd_service_systemd_install_options</b></td><td>Dictionary of entries for the [Install] section of the systemd unit.<br>
Typically includes settings like WantedBy=multi-user.target.<br>
These are merged with the default options defined in docker_systemd_service_systemd_install_options_default.<br></td></tr>
<tr><td><b>docker_systemd_service_start</b></td><td>If true, ensures the systemd service is started and enabled.<br>
If false, the service will be enabled, but not started.<br>
This allows for manual start control after deployment.<br></td></tr>
<tr><td><b>docker_systemd_service_extra_files</b></td><td>List of extra files to copy to te target host, that are required by the service.<br>
Each item should be a dictionary like:<br>
- src: path/to/source/file<br>
dest: path/to/destination/file<br>
mode: '0644'  # Optional, default is '0644'<br>
owner: 'user'  # Optional, default is 'root'<br>
group: 'group'  # Optional, default is 'root'<br>
on_change: 'restart'  # Optional, can be 'restart' or 'reload', default is 'restart'<br>
Sources can be any type of file, directory or jinja2 templates.<br>
Destination should match the type of the source.<br>
Jinja2 templates inside of a directory that would be copied over are also templated, and their .j2 extensions will be stripped out.<br>
If the source is a directory, it will be copied recursively.<br>
If the source is a file, it will be copied as is.<br>
If the source is a jinja2 template, it will be rendered and copied to the destination.<br></td></tr>
<tr><td><b>docker_systemd_service_action</b></td><td>Specifies the action to perform with the systemd service.<br>
Options include 'install', 'uninstall'.<br>
Default is 'install', which sets up the service.<br>
'uninstall' will remove the service and its associated files.<br>
This is useful for cleanup or redeployment scenarios.<br></td></tr>
</table>
<br>
</details>


### Vars

**These are variables with higher priority**
#### File: vars/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [docker_systemd_service_sysconf_dir](vars/main.yml#L9)   | str | `/etc/default` |    false  |  Systemd sysconfig directory |
| [docker_systemd_service_docker_path](vars/main.yml#L16)   | str | `/usr/bin/docker` |    false  |  Docker binary path |
| [docker_systemd_service_systemd_unit_options_default](vars/main.yml#L23)   | dict | `{}` |    false  |  Default systemd unit options |
| [docker_systemd_service_systemd_unit_options_default.**Requires**](vars/main.yml#L24)   | str | `multi-user.target` |    None  |  None |
| [docker_systemd_service_systemd_unit_options_default.**After**](vars/main.yml#L25)   | str | `docker.service` |    None  |  None |
| [docker_systemd_service_systemd_unit_options_default.**PartOf**](vars/main.yml#L26)   | str | `docker.service` |    None  |  None |
| [docker_systemd_service_systemd_service_options_default](vars/main.yml#L34)   | dict | `{}` |    false  |  Default systemd service options |
| [docker_systemd_service_systemd_service_options_default.**EnvironmentFile**](vars/main.yml#L35)   | str | `{{ docker_systemd_service_sysconf_dir }}/{{ docker_systemd_service_name }}` |    None  |  None |
| [docker_systemd_service_systemd_service_options_default.**ExecStartPre**](vars/main.yml#L36)   | str | `-{{ docker_systemd_service_docker_path }} rm -f {{ docker_systemd_service_container_name }}` |    None  |  None |
| [docker_systemd_service_systemd_service_options_default.**ExecStart**](vars/main.yml#L37)   | str | `<multiline value: literal>` |    None  |  None |
| [docker_systemd_service_systemd_service_options_default.**ExecStop**](vars/main.yml#L43)   | str | `{{ docker_systemd_service_docker_path }} stop {{ docker_systemd_service_container_name }}` |    None  |  None |
| [docker_systemd_service_systemd_service_options_default.**ExecReload**](vars/main.yml#L44)   | str | `{{ docker_systemd_service_docker_path }} kill --signal=SIGHUP {{ docker_systemd_service_container_name }}` |    None  |  None |
| [docker_systemd_service_systemd_service_options_default.**Restart**](vars/main.yml#L45)   | str | `always` |    None  |  None |
| [docker_systemd_service_systemd_service_options_default.**RestartSec**](vars/main.yml#L46)   | str | `10s` |    None  |  None |
| [docker_systemd_service_systemd_service_options_default.**SyslogIdentifier**](vars/main.yml#L47)   | str | `{{ docker_systemd_service_container_name }}` |    None  |  None |
| [docker_systemd_service_systemd_install_options_default](vars/main.yml#L55)   | dict | `{}` |    false  |  Default systemd install options |
| [docker_systemd_service_systemd_install_options_default.**WantedBy**](vars/main.yml#L56)   | list | `[]` |    None  |  None |
| [docker_systemd_service_systemd_install_options_default.WantedBy.**0**](vars/main.yml#L57)   | str | `multi-user.target` |    None  |  None |
<details>
<summary><b>🖇️ Full Descriptions for vars in vars/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>docker_systemd_service_sysconf_dir</b></td><td>Defines the directory where environment variable files for systemd are stored.<br>
Typically this is /etc/default on Debian-based systems.<br></td></tr>
<tr><td><b>docker_systemd_service_docker_path</b></td><td>Absolute path to the Docker CLI executable on the target system.<br>
Adjust if using a non-standard Docker installation.<br></td></tr>
<tr><td><b>docker_systemd_service_systemd_unit_options_default</b></td><td>Dictionary of default options for the [Unit] section of the systemd unit file.<br>
Controls dependencies and ordering of the Docker container unit.<br></td></tr>
<tr><td><b>docker_systemd_service_systemd_service_options_default</b></td><td>Dictionary of default options for the [Service] section of the systemd unit file.<br>
Includes the full `ExecStart` command that runs the container and other service behaviors.<br>
Most options should not be overridden unless you need specific behavior.<br></td></tr>
<tr><td><b>docker_systemd_service_systemd_install_options_default</b></td><td>Dictionary of default entries for the [Install] section of the systemd unit file.<br>
Specifies the target under which the service should be enabled.<br>
For repeated options, the expected is a list of values (eg. WantedBy).<br></td></tr>
</table>
<br>
</details>


### Tasks


#### File: tasks/configure.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Docker systemd service ¦ Create ENV file(s) for docker service(s) | ansible.builtin.template | False |
| Docker systemd service ¦ Pull docker image(s) | community.docker.docker_image | True |
| Docker systemd service ¦ Merge user defined systemd unit options with defaults | ansible.builtin.set_fact | False |
| Docker systemd service ¦ Merge user defined systemd service options with defaults | ansible.builtin.set_fact | False |
| Docker systemd service ¦ Merge user defined systemd install options with defaults | ansible.builtin.set_fact | False |
| Docker systemd service ¦ Create unit file(s) for service(s) | ansible.builtin.template | False |
| Docker systemd service ¦ Copy extra configuration files | block | True |
| Docker systemd service ¦ Populate empty on_change list | ansible.builtin.set_fact | False |
| Docker systemd service ¦ Get extra file types | ansible.builtin.stat | False |
| Docker systemd service ¦ Set list for file sources | ansible.builtin.set_fact | True |
| Docker systemd service ¦ Set list for directory sources | ansible.builtin.set_fact | True |
| Docker systemd service ¦ Template extra file sources | ansible.builtin.template | True |
| Docker systemd service ¦ Populate on_change list for extra files | ansible.builtin.set_fact | True |
| Docker systemd service ¦ Template extra directory sources | ansible.builtin.include_tasks | True |
| Docker systemd service ¦ Set reload-check & restart-check variable | ansible.builtin.set_fact | False |
| Docker systemd service ¦ Set reload-check & restart-check variable | ansible.builtin.set_fact | False |
| Docker systemd service ¦ Set reload-check & restart-check variable | ansible.builtin.set_fact | True |

#### File: tasks/main.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Docker systemd service ¦ Set reload-check & restart-check variable | ansible.builtin.set_fact | False |
| Docker systemd service ¦ Install systemd service | block | True |
| Docker systemd service ¦ Import configure.yml | ansible.builtin.include_tasks | False |
| Docker systemd service ¦ Populate service facts | ansible.builtin.service_facts | False |
| Docker systemd service ¦ Set restart-check variable | ansible.builtin.set_fact | True |
| Docker systemd service ¦ Enable service: {{ docker_systemd_service_name }} | ansible.builtin.service | False |
| Docker systemd service ¦ Reload systemd daemon | ansible.builtin.systemd | True |
| Docker systemd service ¦ Start service: {{ docker_systemd_service_name }} | ansible.builtin.service | True |
| Docker systemd service ¦ Reload service: {{ docker_systemd_service_name }} | ansible.builtin.service | True |
| Docker systemd service ¦ Uninstall systemd service | ansible.builtin.include_tasks | True |

#### File: tasks/recursive_copy_extra_dirs.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Docker systemd service ¦ Ensure destination directory exists | ansible.builtin.file | False |
| Docker systemd service ¦ Create extra directory sources | ansible.builtin.file | True |
| Docker systemd service ¦ Template extra directory sources | ansible.builtin.template | True |
| Docker systemd service ¦ Populate on_change list for extra directories | ansible.builtin.set_fact | True |

#### File: tasks/uninstall.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Docker systemd service ¦ Populate service facts | ansible.builtin.service_facts | False |
| Docker systemd service ¦ Stop and disable: {{ docker_systemd_service_name }} | ansible.builtin.systemd | True |
| Docker systemd service ¦ Remove systemd service file | ansible.builtin.file | False |
| Docker systemd service ¦ Remove ENV file | ansible.builtin.file | False |
| Docker systemd service ¦ Reload systemd daemon | ansible.builtin.systemd | True |







## Author Information
Bertrand Lanson

#### License

license (BSD, MIT)

#### Minimum Ansible Version

2.10

#### Platforms

- **Ubuntu**: ['focal', 'jammy', 'noble']
- **Debian**: ['bullseye', 'bookworm']


#### Dependencies

No dependencies specified.
<!-- DOCSIBLE END -->
