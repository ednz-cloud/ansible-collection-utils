<!-- DOCSIBLE START -->

# 📃 Role overview

## manage_pip_packages



Description: Package management for python on debian-based distros.


| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 09/07/2025 |








### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [manage_pip_packages_install_prereqs](defaults/main.yml#L9)   | bool | `True` |    false  |  Install prerequisites |
| [manage_pip_packages_list](defaults/main.yml#L18)   | list | `[]` |    false  |  List of pip packages to manage |
| [manage_pip_packages_break_system_packages](defaults/main.yml#L25)   | bool | `False` |    false  |  Break system packages |
| [manage_pip_packages_create_venv](defaults/main.yml#L32)   | bool | `False` |    false  |  Create a virtual environment |
| [manage_pip_packages_venv_path](defaults/main.yml#L39)   | str | `/tmp/venv` |    false  |  Virtual environment path |
| [manage_pip_packages_venv_inherit_global](defaults/main.yml#L46)   | bool | `False` |    false  |  Inherit global site packages |
<details>
<summary><b>🖇️ Full descriptions for vars in defaults/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>manage_pip_packages_install_prereqs</b></td><td>Determines whether prerequisite system packages (like Python, pip) should be installed.<br>
Set to true to ensure the system can install and manage pip packages.<br></td></tr>
<tr><td><b>manage_pip_packages_list</b></td><td>List of pip packages to install, uninstall, or ensure are at specific versions.<br>
Each entry should be a dictionary with the keys: 'name', 'version_constraint', and 'state'.<br>
'version_constraint' can be a specific version or 'latest'.<br>
'state' can be 'present', 'absent', or 'latest'.<br></td></tr>
<tr><td><b>manage_pip_packages_break_system_packages</b></td><td>If true, allows pip to install packages even if it might overwrite or conflict with system packages.<br>
Useful in some cases but should be used with caution.<br></td></tr>
<tr><td><b>manage_pip_packages_create_venv</b></td><td>Whether to create and use a Python virtual environment for package installation.<br>
This helps isolate package installations from the system Python environment.<br></td></tr>
<tr><td><b>manage_pip_packages_venv_path</b></td><td>Filesystem path to create the virtual environment in.<br>
Used only if 'manage_pip_packages_create_venv' is true.<br></td></tr>
<tr><td><b>manage_pip_packages_venv_inherit_global</b></td><td>Determines whether the virtual environment should have access to global site-packages.<br>
Set to true to allow the virtual environment to see globally installed packages.<br></td></tr>
</table>
<br>
</details>


### Vars

**These are variables with higher priority**
#### File: vars/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [manage_pip_packages_required_packages](vars/main.yml#L9)   | list | `[]` |    true  |  Required system packages |
| [manage_pip_packages_required_packages.**0**](vars/main.yml#L10)   | dict | `{}` |    None  |  None |
| [manage_pip_packages_required_packages.0.**name**](vars/main.yml#L10)   | str | `python3` |    None  |  None |
| [manage_pip_packages_required_packages.0.**version**](vars/main.yml#L11)   | str | `latest` |    None  |  None |
| [manage_pip_packages_required_packages.0.**state**](vars/main.yml#L12)   | str | `present` |    None  |  None |
| [manage_pip_packages_required_packages.**1**](vars/main.yml#L13)   | dict | `{}` |    None  |  None |
| [manage_pip_packages_required_packages.1.**name**](vars/main.yml#L13)   | str | `python3-pip` |    None  |  None |
| [manage_pip_packages_required_packages.1.**version**](vars/main.yml#L14)   | str | `latest` |    None  |  None |
| [manage_pip_packages_required_packages.1.**state**](vars/main.yml#L15)   | str | `present` |    None  |  None |
| [manage_pip_packages_venv_required_packages](vars/main.yml#L22)   | list | `[]` |    true  |  Virtual environment packages |
| [manage_pip_packages_venv_required_packages.**0**](vars/main.yml#L23)   | dict | `{}` |    None  |  None |
| [manage_pip_packages_venv_required_packages.0.**name**](vars/main.yml#L23)   | str | `python3-venv` |    None  |  None |
| [manage_pip_packages_venv_required_packages.0.**version**](vars/main.yml#L24)   | str | `latest` |    None  |  None |
| [manage_pip_packages_venv_required_packages.0.**state**](vars/main.yml#L25)   | str | `present` |    None  |  None |
| [manage_pip_packages_venv_python_path](vars/main.yml#L32)   | str | `{{ manage_pip_packages_venv_path }}/bin/python3` |    false  |  Python binary path in virtual environment |
| [manage_pip_packages_venv_command](vars/main.yml#L39)   | str | `{{ ansible_python_interpreter ¦ default('/usr/bin/python3') }} -m venv` |    false  |  Virtual environment creation command |
<details>
<summary><b>🖇️ Full Descriptions for vars in vars/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>manage_pip_packages_required_packages</b></td><td>List of system-level packages required to install and manage pip.<br>
These packages will be installed before managing any pip packages.<br></td></tr>
<tr><td><b>manage_pip_packages_venv_required_packages</b></td><td>List of packages required to support virtual environment creation.<br>
Only installed if 'manage_pip_packages_create_venv' is true.<br></td></tr>
<tr><td><b>manage_pip_packages_venv_python_path</b></td><td>Path to the Python interpreter within the created virtual environment.<br>
Used when installing packages inside the venv.<br></td></tr>
<tr><td><b>manage_pip_packages_venv_command</b></td><td>Command used to create the virtual environment.<br>
Defaults to using the current Python interpreter with the '-m venv' module.<br></td></tr>
</table>
<br>
</details>


### Tasks


#### File: tasks/main.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Import prerequisites.yml | ansible.builtin.include_tasks | True |
| Install/remove required pip packages | ansible.builtin.pip | True |

#### File: tasks/prerequisites.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Pip3 ¦ Merge required system package lists | ansible.builtin.set_fact | False |
| Install python3 and pip | ansible.builtin.include_role | False |







## Author Information
Bertrand Lanson

#### License

license (BSD, MIT)

#### Minimum Ansible Version

2.10

#### Platforms

- **Ubuntu**: ['noble', 'focal', 'jammy']
- **Debian**: ['bullseye', 'bookworm']


#### Dependencies

No dependencies specified.
<!-- DOCSIBLE END -->
