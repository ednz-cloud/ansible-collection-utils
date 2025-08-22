<!-- DOCSIBLE START -->

# 📃 Role overview

## manage_apt_packages



Description: Package management for debian-based distros.


| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 25/06/2025 |








### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [manage_apt_packages_list](defaults/main.yml#L15)   | list | `[]` |    false  |  List of packages to manage |
<details>
<summary><b>🖇️ Full descriptions for vars in defaults/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>manage_apt_packages_list</b></td><td>List of packages to manage with<br>
This list is used to install, update, or remove packages.<br>
Each item should be a dictionary with keys:<br>
- name: Name of the package (e.g., 'nginx')<br>
- version: Version to install (optional, default is 'latest')<br>
- state: Desired state of the package (e.g., 'present', 'absent', 'latest')<br>
If 'version' is not specified, the latest version will be installed.<br>
If 'state' is not specified, it defaults to 'present'.<br></td></tr>
</table>
<br>
</details>


### Vars

**These are variables with higher priority**
#### File: vars/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [manage_apt_packages_apt_cache_time](vars/main.yml#L10)   | int | `3600` |    false  |  Cache time for apt package management |
<details>
<summary><b>🖇️ Full Descriptions for vars in vars/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>manage_apt_packages_apt_cache_time</b></td><td>Time in seconds for which the apt cache is considered valid.<br>
This is used to avoid frequent updates of the apt cache.<br>
If not specified, it defaults to 3600 seconds (1 hour).<br></td></tr>
</table>
<br>
</details>


### Tasks


#### File: tasks/main.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Update apt caches | ansible.builtin.apt | False |
| Install/remove required apt packages | ansible.builtin.apt | True |







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
