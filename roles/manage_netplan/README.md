<!-- DOCSIBLE START -->

# 📃 Role overview

## manage_netplan



Description: Install and configure network interfaces using netplan for debian-based distros.


| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 22/06/2025 |








### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [manage_netplan_config_file](defaults/main.yml#L9)   | str | `/etc/netplan/ansible-config.yaml` |    false  |  Netplan configuration file |
| [manage_netplan_renderer](defaults/main.yml#L16)   | str | `networkd` |    false  |  Netplan renderer |
| [manage_netplan_remove_existing](defaults/main.yml#L23)   | bool | `False` |    false  |  Remove existing configurations |
| [manage_netplan_install](defaults/main.yml#L30)   | bool | `True` |    false  |  Manage Netplan installation |
| [manage_netplan_apply](defaults/main.yml#L37)   | bool | `False` |    false  |  Apply Netplan configuration |
| [manage_netplan_configuration](defaults/main.yml#L44)   | dict | `{}` |    true  |  Netplan configuration |
<details>
<summary><b>🖇️ Full descriptions for vars in defaults/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>manage_netplan_config_file</b></td><td>Specifies the file path for the Netplan configuration.<br>
The file must have a .yaml extension, as some Netplan versions may not support .yml.<br></td></tr>
<tr><td><b>manage_netplan_renderer</b></td><td>Defines the backend used by Netplan to apply network settings.<br>
Possible values are 'NetworkManager' or 'networkd'.<br></td></tr>
<tr><td><b>manage_netplan_remove_existing</b></td><td>Determines whether to delete all existing Netplan configurations before applying new ones.<br>
Set to true to remove all configurations in /etc/netplan.<br></td></tr>
<tr><td><b>manage_netplan_install</b></td><td>Controls whether the Netplan package should be installed.<br>
Set to true to ensure Netplan is installed.<br></td></tr>
<tr><td><b>manage_netplan_apply</b></td><td>Specifies whether to apply the Netplan configuration after changes are made.<br>
Set to true to automatically apply the configuration.<br></td></tr>
<tr><td><b>manage_netplan_configuration</b></td><td>Defines the Netplan configuration as a dictionary.<br>
Use this to specify the desired network settings.<br></td></tr>
</table>
<br>
</details>


### Vars

**These are variables with higher priority**
#### File: vars/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [manage_netplan_packages](vars/main.yml#L7)   | list | `[]` |    false  |  Netplan packages |
| [manage_netplan_packages.**0**](vars/main.yml#L8)   | dict | `{}` |    None  |  None |
| [manage_netplan_packages.0.**name**](vars/main.yml#L8)   | str | `netplan.io` |    None  |  None |
| [manage_netplan_packages.0.**version**](vars/main.yml#L9)   | str | `latest` |    None  |  None |
| [manage_netplan_packages.0.**state**](vars/main.yml#L10)   | str | `present` |    None  |  None |
| [manage_netplan_networkmanager_pkg](vars/main.yml#L15)   | list | `[]` |    false  |  NetworkManager packages |
| [manage_netplan_networkmanager_pkg.**0**](vars/main.yml#L16)   | dict | `{}` |    None  |  None |
| [manage_netplan_networkmanager_pkg.0.**name**](vars/main.yml#L16)   | str | `network` |    None  |  None |
| [manage_netplan_networkmanager_pkg.0.**version**](vars/main.yml#L17)   | str | `latest` |    None  |  None |
| [manage_netplan_networkmanager_pkg.0.**state**](vars/main.yml#L18)   | str | `present` |    None  |  None |
<details>
<summary><b>🖇️ Full Descriptions for vars in vars/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>manage_netplan_packages</b></td><td>List of packages necessary for Netplan functionality</td></tr>
<tr><td><b>manage_netplan_networkmanager_pkg</b></td><td>List of packages required to enable NetworkManager functionality</td></tr>
</table>
<br>
</details>


### Tasks


#### File: tasks/configure.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Netplan ¦ Copy netplan configuration template into {{ manage_netplan_config_file }} | ansible.builtin.template | True |
| Netplan ¦ Set generate-check and apply-check variables | ansible.builtin.set_fact | True |

#### File: tasks/install.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Netplan ¦ Install netplan:latest | ansible.builtin.include_role | False |
| Netplan ¦ Install network-manager:latest when used as renderer | ansible.builtin.include_role | True |
| Netplan ¦ Create directory /etc/netplan | ansible.builtin.file | False |

#### File: tasks/main.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Netplan ¦ Set generate-check and apply-check variables | ansible.builtin.set_fact | False |
| Netplan ¦ Import install.yml | ansible.builtin.include_tasks | True |
| Netplan ¦ Import remove_existing.yml | ansible.builtin.include_tasks | True |
| Netplan ¦ Import configure.yml | ansible.builtin.include_tasks | False |
| Netplan ¦ Generate netplan configuration | ansible.builtin.command | True |
| Netplan ¦ Apply netplan configuration | ansible.builtin.command | True |

#### File: tasks/remove_existing.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Netplan ¦ Fetch existing configurations | ansible.builtin.find | False |
| Netplan ¦ Remove existing configurations | ansible.builtin.file | True |







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
