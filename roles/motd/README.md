<!-- DOCSIBLE START -->

# 📃 Role overview

## motd



Description: Simple role to configure a Message Of The Day (MOTD) with ASCII logo and system information.


| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 31/08/2025 |








### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [motd_ascii_file_source](defaults/main.yml#L9)   | str | `00-ednz-cloud.j2` |    false  |  motd ascii logo source file |
| [motd_sysinfo_color](defaults/main.yml#L17)   | str | `green` |    false  |  motd sysinfo color |
| [motd_production_warning](defaults/main.yml#L24)   | bool | `False` |    false  |  motd production warning |
<details>
<summary><b>🖇️ Full descriptions for vars in defaults/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>motd_ascii_file_source</b></td><td>Template file to use as the source for the ASCII logo displayed in the MOTD.<br>
This can should be a Jinja2 template.<br></td></tr>
<tr><td><b>motd_sysinfo_color</b></td><td>Color to use for the system information in the MOTD.<br>
Valid colors are: black, red, green, yellow, blue, purple, cyan,<br>
light_cyan, white<br></td></tr>
<tr><td><b>motd_production_warning</b></td><td>Whether to display a production warning in the MOTD.<br>
This is useful for production systems to remind users to be careful.<br></td></tr>
</table>
<br>
</details>


### Vars

**These are variables with higher priority**
#### File: vars/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [motd_directory_path](vars/main.yml#L9)   | str | `/etc/update-motd.d` |    false  |  motd directory path |
| [motd_ascii_file](vars/main.yml#L16)   | str | `00-ascii-logo` |    false  |  motd ascii file |
| [motd_sysinfo_file](vars/main.yml#L23)   | str | `10-sysinfo` |    false  |  motd sysinfo file |
| [motd_production_warning_file](vars/main.yml#L30)   | str | `99-production-warning` |    false  |  motd production warning file |
| [motd_filenames](vars/main.yml#L37)   | list | `[]` |    false  |  motd filenames |
| [motd_filenames.**0**](vars/main.yml#L38)   | str | `{{ motd_ascii_file }}` |    None  |  None |
| [motd_filenames.**1**](vars/main.yml#L39)   | str | `{{ motd_sysinfo_file }}` |    None  |  None |
| [motd_filenames.**2**](vars/main.yml#L40)   | str | `{{ motd_production_warning_file }}` |    None  |  None |
| [motd_color_map](vars/main.yml#L47)   | dict | `{}` |    false  |  motd color map |
| [motd_color_map.**black**](vars/main.yml#L48)   | str | `[0;30m` |    None  |  None |
| [motd_color_map.**red**](vars/main.yml#L49)   | str | `[0;31m` |    None  |  None |
| [motd_color_map.**green**](vars/main.yml#L50)   | str | `[0;32m` |    None  |  None |
| [motd_color_map.**yellow**](vars/main.yml#L51)   | str | `[1;33m` |    None  |  None |
| [motd_color_map.**blue**](vars/main.yml#L52)   | str | `[0;34m` |    None  |  None |
| [motd_color_map.**purple**](vars/main.yml#L53)   | str | `[0;35m` |    None  |  None |
| [motd_color_map.**cyan**](vars/main.yml#L54)   | str | `[0;36m` |    None  |  None |
| [motd_color_map.**light_cyan**](vars/main.yml#L55)   | str | `[1;36m` |    None  |  None |
| [motd_color_map.**white**](vars/main.yml#L56)   | str | `[1;37m` |    None  |  None |
<details>
<summary><b>🖇️ Full Descriptions for vars in vars/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>motd_directory_path</b></td><td>Path to the directory where the MOTD scripts are stored.<br>
Default is /etc/update-motd.d<br></td></tr>
<tr><td><b>motd_ascii_file</b></td><td>Filename for the ASCII logo script in the MOTD on the target system.<br>
Default is 00-ascii-logo<br></td></tr>
<tr><td><b>motd_sysinfo_file</b></td><td>Filename for the system information script in the MOTD on the target system.<br>
Default is 10-sysinfo<br></td></tr>
<tr><td><b>motd_production_warning_file</b></td><td>Filename for the production warning script in the MOTD on the target system.<br>
Default is 99-production-warning<br></td></tr>
<tr><td><b>motd_filenames</b></td><td>List of filenames to manage in the MOTD directory.<br>
This is derived from the individual filename variables.<br></td></tr>
<tr><td><b>motd_color_map</b></td><td>Mapping of color names to ANSI color codes for use in the MOTD.<br>
This is used to set the color of the system information in the MOTD.<br></td></tr>
</table>
<br>
</details>


### Tasks


#### File: tasks/main.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| Import prerequisites.yml | ansible.builtin.include_tasks | False |
| MOTD ¦ Deploy ASCII logo script | ansible.builtin.template | False |
| MOTD ¦ Deploy system info script | ansible.builtin.template | False |
| MOTD ¦ Handle  production warning script | block | False |
| MOTD ¦ Deploy production warning script | ansible.builtin.template | True |
| MOTD ¦ Remove production warning script | ansible.builtin.file | True |

#### File: tasks/prerequisites.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| MOTD ¦ Ensure directory exists: {{ motd_directory_path }} | ansible.builtin.file | False |
| MOTD ¦ Ensure no other files are in motd | block | False |
| MOTD ¦ Collect files in motd dir | ansible.builtin.find | False |
| MOTD ¦ Collect dir in motd dir | ansible.builtin.find | False |
| MOTD ¦ Remove all unwanted files and directories | ansible.builtin.file | True |
| MOTD ¦ Remove /etc/motd file | ansible.builtin.file | False |







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
