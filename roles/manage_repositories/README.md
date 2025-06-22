<!-- DOCSIBLE START -->

# 📃 Role overview

## manage_repositories



Description: Repository management for debian-based distros.


| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 22/06/2025 |








### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [manage_repositories_enable_default_repo](defaults/main.yml#L9)   | bool | `True` |    false  |  Enable or disable the default repository management. |
| [manage_repositories_main_repo_uri](defaults/main.yml#L16)   | dict | `{}` |    true  |  The main repository URI for the distribution. |
| [manage_repositories_main_repo_uri.**ubuntu**](defaults/main.yml#L17)   | str | `http://fr.archive.ubuntu.com/ubuntu` |    None  |  None |
| [manage_repositories_main_repo_uri.**debian**](defaults/main.yml#L18)   | str | `http://deb.debian.org/debian` |    None  |  None |
| [manage_repositories_enable_custom_repo](defaults/main.yml#L24)   | bool | `False` |    false  |  Enable or disable the custom repository management. |
| [manage_repositories_custom_repo](defaults/main.yml#L50)   | list | `[]` |    false  |  Custom repositories to be managed. |
<details>
<summary><b>🖇️ Full descriptions for vars in defaults/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>manage_repositories_enable_default_repo</b></td><td>Enable or disable the default repository management.<br>
If set to true, the default repositories for the distribution will be managed.<br></td></tr>
<tr><td><b>manage_repositories_main_repo_uri</b></td><td>The main repository URI for the distribution.<br>
This is used to set the main repository for the distribution.<br></td></tr>
<tr><td><b>manage_repositories_enable_custom_repo</b></td><td>Enable or disable the custom repository management.<br></td></tr>
<tr><td><b>manage_repositories_custom_repo</b></td><td>A list of custom repositories to be managed.<br>
Each repository should be a dictionary with the following keys:<br>
- name: The name of the repository.<br>
- uri: The URI of the repository.<br>
- comments: A comment for the repository.<br>
- types: The types of the repository (e.g., deb, rpm).<br>
- suites: The suites of the repository (e.g., stable, testing).<br>
- components: The components of the repository (e.g., main, universe).<br>
- signed_by: The URI of the GPG key for the repository. (optional).<br>
See the deb822 module documentation for more details.<br>
Example:<br>
- name: docker<br>
uri: "https://download.docker.com/linux/{{ ansible_distribution|lower }}"<br>
comments: "{{ ansible_distribution|lower }} docker repository"<br>
types:<br>
- deb<br>
suites:<br>
- "{{ ansible_distribution_release }}"<br>
components:<br>
- stable<br>
signed_by: "https://download.docker.com/linux/{{ ansible_distribution|lower }}/gpg"<br></td></tr>
</table>
<br>
</details>


### Vars

**These are variables with higher priority**
#### File: vars/debian.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [manage_repositories_default_repo](vars/debian.yml#L7)   | list | `[]` |    true  |  Default repository configuration for Debian distributions. |
| [manage_repositories_default_repo.**0**](vars/debian.yml#L8)   | dict | `{}` |    None  |  None |
| [manage_repositories_default_repo.0.**name**](vars/debian.yml#L8)   | str | `debian` |    None  |  None |
| [manage_repositories_default_repo.0.**uri**](vars/debian.yml#L9)   | str | `{{ manage_repositories_main_repo_uri[ansible_distribution¦lower] }}` |    None  |  None |
| [manage_repositories_default_repo.0.**comments**](vars/debian.yml#L10)   | str | `debian main repository` |    None  |  None |
| [manage_repositories_default_repo.0.**types**](vars/debian.yml#L11)   | list | `[]` |    None  |  None |
| [manage_repositories_default_repo.0.types.**0**](vars/debian.yml#L12)   | str | `deb` |    None  |  None |
| [manage_repositories_default_repo.0.**suites**](vars/debian.yml#L13)   | list | `[]` |    None  |  None |
| [manage_repositories_default_repo.0.suites.**0**](vars/debian.yml#L14)   | str | `{{ ansible_distribution_release }}` |    None  |  None |
| [manage_repositories_default_repo.0.suites.**1**](vars/debian.yml#L15)   | str | `{{ ansible_distribution_release }}-updates` |    None  |  None |
| [manage_repositories_default_repo.0.suites.**2**](vars/debian.yml#L16)   | str | `{{ ansible_distribution_release }}-backports` |    None  |  None |
| [manage_repositories_default_repo.0.**components**](vars/debian.yml#L17)   | list | `[]` |    None  |  None |
| [manage_repositories_default_repo.0.components.**0**](vars/debian.yml#L18)   | str | `main` |    None  |  None |
| [manage_repositories_default_repo.**1**](vars/debian.yml#L19)   | dict | `{}` |    None  |  None |
| [manage_repositories_default_repo.1.**name**](vars/debian.yml#L19)   | str | `debian-security` |    None  |  None |
| [manage_repositories_default_repo.1.**uri**](vars/debian.yml#L20)   | str | `{{ manage_repositories_main_repo_uri[ansible_distribution¦lower] }}-security` |    None  |  None |
| [manage_repositories_default_repo.1.**comments**](vars/debian.yml#L21)   | str | `debian main repository` |    None  |  None |
| [manage_repositories_default_repo.1.**types**](vars/debian.yml#L22)   | list | `[]` |    None  |  None |
| [manage_repositories_default_repo.1.types.**0**](vars/debian.yml#L23)   | str | `deb` |    None  |  None |
| [manage_repositories_default_repo.1.**suites**](vars/debian.yml#L24)   | list | `[]` |    None  |  None |
| [manage_repositories_default_repo.1.suites.**0**](vars/debian.yml#L25)   | str | `{{ ansible_distribution_release }}-security` |    None  |  None |
| [manage_repositories_default_repo.1.**components**](vars/debian.yml#L26)   | list | `[]` |    None  |  None |
| [manage_repositories_default_repo.1.components.**0**](vars/debian.yml#L27)   | str | `main` |    None  |  None |
#### File: vars/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [manage_repositories_sources_list_location](vars/main.yml#L7)   | str | `/etc/apt/sources.list` |    true  |  Location of the sources list file. |
| [manage_repositories_repo_location](vars/main.yml#L12)   | str | `/etc/apt/sources.list.d` |    true  |  Location of the repository files. |
| [manage_repositories_signing_keys_location](vars/main.yml#L17)   | str | `/usr/share/keyrings` |    true  |  Location of the signing keys. |
| [manage_repositories_sources_list_message](vars/main.yml#L22)   | str | `# See /etc/apt/sources.list.d/{{ ansible_distribution¦lower }}.sources\n` |    true  |  Comment for the sources list file. |
| [manage_repositories_required_packages](vars/main.yml#L27)   | list | `[]` |    true  |  Required packages for managing repositories. |
| [manage_repositories_required_packages.**0**](vars/main.yml#L27)   | str | `python3-debian` |    true  |  Required packages for managing repositories. |
#### File: vars/ubuntu.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [manage_repositories_default_repo](vars/ubuntu.yml#L7)   | list | `[]` |    true  |  Default repository configuration for Ubuntu distributions. |
| [manage_repositories_default_repo.**0**](vars/ubuntu.yml#L8)   | dict | `{}` |    None  |  None |
| [manage_repositories_default_repo.0.**name**](vars/ubuntu.yml#L8)   | str | `ubuntu` |    None  |  None |
| [manage_repositories_default_repo.0.**uri**](vars/ubuntu.yml#L9)   | str | `{{ manage_repositories_main_repo_uri[ansible_distribution¦lower] }}` |    None  |  None |
| [manage_repositories_default_repo.0.**comments**](vars/ubuntu.yml#L10)   | str | `ubuntu main repository` |    None  |  None |
| [manage_repositories_default_repo.0.**types**](vars/ubuntu.yml#L11)   | list | `[]` |    None  |  None |
| [manage_repositories_default_repo.0.types.**0**](vars/ubuntu.yml#L12)   | str | `deb` |    None  |  None |
| [manage_repositories_default_repo.0.**suites**](vars/ubuntu.yml#L13)   | list | `[]` |    None  |  None |
| [manage_repositories_default_repo.0.suites.**0**](vars/ubuntu.yml#L14)   | str | `{{ ansible_distribution_release }}` |    None  |  None |
| [manage_repositories_default_repo.0.suites.**1**](vars/ubuntu.yml#L15)   | str | `{{ ansible_distribution_release }}-security` |    None  |  None |
| [manage_repositories_default_repo.0.suites.**2**](vars/ubuntu.yml#L16)   | str | `{{ ansible_distribution_release }}-updates` |    None  |  None |
| [manage_repositories_default_repo.0.suites.**3**](vars/ubuntu.yml#L17)   | str | `{{ ansible_distribution_release }}-backports` |    None  |  None |
| [manage_repositories_default_repo.0.**components**](vars/ubuntu.yml#L18)   | list | `[]` |    None  |  None |
| [manage_repositories_default_repo.0.components.**0**](vars/ubuntu.yml#L19)   | str | `main` |    None  |  None |
| [manage_repositories_default_repo.0.components.**1**](vars/ubuntu.yml#L20)   | str | `restricted` |    None  |  None |
| [manage_repositories_default_repo.0.components.**2**](vars/ubuntu.yml#L21)   | str | `universe` |    None  |  None |
| [manage_repositories_default_repo.0.components.**3**](vars/ubuntu.yml#L22)   | str | `multiverse` |    None  |  None |
<details>
<summary><b>🖇️ Full Descriptions for vars in vars/debian.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>manage_repositories_default_repo</b></td><td>This variable defines the default repositories for Debian distributions.</td></tr>
</table>
<br>
</details>
<details>
<summary><b>🖇️ Full Descriptions for vars in vars/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>manage_repositories_sources_list_location</b></td><td>This variable defines the location of the sources list file for the package manager.</td></tr>
<tr><td><b>manage_repositories_repo_location</b></td><td>This variable defines the location of the repository files for the package manager.</td></tr>
<tr><td><b>manage_repositories_signing_keys_location</b></td><td>This variable defines the location of the signing keys for the package manager.</td></tr>
<tr><td><b>manage_repositories_sources_list_message</b></td><td>This variable defines the comment for the sources list file (because it is not used).</td></tr>
<tr><td><b>manage_repositories_required_packages</b></td><td>This variable defines the packages required for managing repositories.</td></tr>
<tr><td><b>manage_repositories_required_packages.0</b></td><td>This variable defines the packages required for managing repositories.</td></tr>
</table>
<br>
</details>
<details>
<summary><b>🖇️ Full Descriptions for vars in vars/ubuntu.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>manage_repositories_default_repo</b></td><td>This variable defines the default repositories for Ubuntu distributions.</td></tr>
</table>
<br>
</details>


### Tasks


#### File: tasks/custom_repositories.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| APT Repo ¦ Configure custom repositories | ansible.builtin.deb822_repository | False |
| APT Repo ¦ Set cache-update variable | ansible.builtin.set_fact | True |

#### File: tasks/main.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| APT Repo ¦ Set cache-update variable | ansible.builtin.set_fact | False |
| APT Repo ¦ Load variables | ansible.builtin.include_vars | False |
| APT Repo ¦ Import prerequisites.yml | ansible.builtin.include_tasks | False |
| APT Repo ¦ Import main repositories for {{ ansible_distribution¦lower }} | ansible.builtin.include_tasks | True |
| APT Repo ¦ Import custom_repositories.yml | ansible.builtin.include_tasks | True |
| APT Repo ¦ Update apt caches | ansible.builtin.apt | True |

#### File: tasks/main_repositories.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| APT Repo ¦ Emtpy /etc/apt/sources.list | block | False |
| APT Repo ¦ Read the current content of source.list | ansible.builtin.slurp | False |
| APT Repo ¦ Convert sources.list current content to string | ansible.builtin.set_fact | False |
| APT Repo ¦ Define sources.list new content | ansible.builtin.set_fact | False |
| APT Repo ¦ Create file /etc/apt/sources.list | ansible.builtin.file | True |
| APT Repo ¦ Replace content of /etc/apt/sources.list | ansible.builtin.replace | True |
| APT Repo ¦ Configure main repositories into sources.list.d for {{ ansible_distribution¦lower }}  | ansible.builtin.deb822_repository | False |
| APT Repo ¦ Set cache-update variable | ansible.builtin.set_fact | True |

#### File: tasks/prerequisites.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| APT Repo ¦ Update repositories cache | ansible.builtin.apt | False |
| APT Repo ¦ Install required packages | ansible.builtin.apt | False |







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
