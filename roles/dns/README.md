<!-- DOCSIBLE START -->

# 📃 Role overview

## dns



Description: Configure dns resolution for debian-based distros.


| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 05/11/2025 |








### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [dns_resolver_mode](defaults/main.yml#L9)   | str | `systemd` |    true  |  Resolver name |
| [dns_nameservers](defaults/main.yml#L18)   | list | `[]` |    true  |  Nameservers |
| [dns_nameservers.**0**](defaults/main.yml#L19)   | str | `1.1.1.1` |    None  |  None |
| [dns_nameservers.**1**](defaults/main.yml#L20)   | str | `8.8.8.8` |    None  |  None |
| [dns_resolved_conf_options](defaults/main.yml#L30)   | dict | `{}` |    true  |  Resolved options |
| [dns_resolv_conf_search](defaults/main.yml#L37)   | list | `[]` |    true  |  resolv.conf search options |
| [dns_resolv_conf_sortlist](defaults/main.yml#L44)   | list | `[]` |    true  |  resolv.conf sortlist options |
| [dns_resolv_conf_options](defaults/main.yml#L51)   | list | `[]` |    true  |  resolv.conf options |
<details>
<summary><b>🖇️ Full descriptions for vars in defaults/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>dns_resolver_mode</b></td><td>The resolver to use for DNS resolution<br>
Currently supports: systemd, manual<br></td></tr>
<tr><td><b>dns_nameservers</b></td><td>The list of DNS servers to use.<br>
List of 0 to N DNS servers are expected.<br>
Depending on resolver, syntax may vary.<br>
See man resolv.conf, man resolved.conf<br></td></tr>
<tr><td><b>dns_resolved_conf_options</b></td><td>When using the systemd resolver,<br>
A dict of options to pass to the resolved.conf file.<br>
DNS servers are not passed by default to avoid colliding<br>
with dhcp-served servers.<br>
See man resolved.conf for more infos<br></td></tr>
<tr><td><b>dns_resolv_conf_search</b></td><td>When using the manual resolver,<br>
a list of search domains.<br></td></tr>
<tr><td><b>dns_resolv_conf_sortlist</b></td><td>When using the manual resolver,<br>
a list of sortlists.<br></td></tr>
<tr><td><b>dns_resolv_conf_options</b></td><td>When using the manual resolver,<br>
a list of options.<br></td></tr>
</table>
<br>
</details>


### Vars

**These are variables with higher priority**
#### File: vars/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|------------|-------------|
| [dns_supported_resolvers](vars/main.yml#L8)   | list | `[]` |    true  |  Supported resolvers |
| [dns_supported_resolvers.**0**](vars/main.yml#L8)   | str | `systemd` |    true  |  Supported resolvers |
| [dns_supported_resolvers.**1**](vars/main.yml#L8)   | str | `manual` |    true  |  Supported resolvers |
| [dns_resolv_conf_path](vars/main.yml#L14)   | str | `/etc/resolv.conf` |    true  |  Path to resolv.conf |
| [dns_systemd_resolved_conf_directory](vars/main.yml#L20)   | str | `/etc/systemd/resolved.conf.d` |    true  |  Path to systemd-resolved configuration |
| [dns_systemd_resolved_package](vars/main.yml#L26)   | str | `systemd-resolved` |    true  |  Package name |
| [dns_systemd_resolved_service](vars/main.yml#L32)   | str | `systemd-resolved.service` |    true  |  Systemd service name |
| [dns_systemd_stub_resolver_enabled](vars/main.yml#L39)   | str | `<multiline value: folded_strip>` |    true  |  Stub resolver enabled |
| [dns_systemd_resolved_stub_file](vars/main.yml#L53)   | str | `<multiline value: folded_strip>` |    true  |  Systemd resolver file |
<details>
<summary><b>🖇️ Full Descriptions for vars in vars/main.yml</b></summary>
<br>
<table>
<th>Var</th><th>Description</th>
<tr><td><b>dns_supported_resolvers</b></td><td>The list of supported resolvers.<br></td></tr>
<tr><td><b>dns_supported_resolvers.0</b></td><td>The list of supported resolvers.<br></td></tr>
<tr><td><b>dns_supported_resolvers.1</b></td><td>The list of supported resolvers.<br></td></tr>
<tr><td><b>dns_resolv_conf_path</b></td><td>Path to resolv.conf file.<br></td></tr>
<tr><td><b>dns_systemd_resolved_conf_directory</b></td><td>Path to systemd-resolved configuration directory.<br></td></tr>
<tr><td><b>dns_systemd_resolved_package</b></td><td>Package name for systemd-resolved.<br></td></tr>
<tr><td><b>dns_systemd_resolved_service</b></td><td>Systemd service name for systemd-resolved.<br></td></tr>
<tr><td><b>dns_systemd_stub_resolver_enabled</b></td><td>Variable for detecting if the stub resolver of systemd-resolved<br>
is in-use. This variable should not be changed.<br></td></tr>
<tr><td><b>dns_systemd_resolved_stub_file</b></td><td>File to symlink to /etc/resolv.conf when resolver is systemd.<br>
Changes based on if the stub-resolver is enabled.<br></td></tr>
</table>
<br>
</details>


### Tasks


#### File: tasks/main.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| DNS ¦ Ensure resolver is supported | ansible.builtin.assert | False |
| DNS ¦ Set reload-check & restart-check variable | ansible.builtin.set_fact | False |
| DNS ¦ Gather service facts | ansible.builtin.service_facts | True |
| DNS ¦ include tasks for resolver: {{ dns_resolver_mode }} | ansible.builtin.include_tasks | False |
| DNS ¦ Reload service: {{ dns_systemd_resolved_service }} | ansible.builtin.service | True |

#### File: tasks/manual.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| DNS ¦ Ensure systemd-resolved is not used | block | True |
| DNS ¦ Stop and disable {{ dns_systemd_resolved_service }} | ansible.builtin.service | False |
| DNS ¦ Copy configuration: {{ dns_resolv_conf_path }} | ansible.builtin.template | False |

#### File: tasks/systemd.yml

| Name | Module | Has Conditions |
| ---- | ------ | -------------- |
| DNS ¦ Ensure systemd-resolved is usable | block | True |
| DNS ¦ Install {{ dns_systemd_resolved_package }} | ansible.builtin.apt | False |
| DNS ¦ Start and enable {{ dns_systemd_resolved_service }} | ansible.builtin.service | False |
| DNS ¦ Ensure systemd-resolved configuration directory exists | ansible.builtin.file | False |
| DNS ¦ Copy systemd-resolved configuration | ansible.builtin.template | False |
| DNS ¦ Get current /etc/resolv.conf state | ansible.builtin.stat | False |
| DNS ¦ Set /etc/resolve.conf file | block | True |
| DNS ¦ Remove incompatible /etc/reoslv.conf file | ansible.builtin.file | True |
| DNS ¦ Ensure /etc/resolv.conf is symlink to correct stub file | ansible.builtin.file | False |
| DNS ¦ Set reload-check & restart-check variable | ansible.builtin.set_fact | True |







## Author Information
Bertrand Lanson

#### License

license (BSD, MIT)

#### Minimum Ansible Version

2.10

#### Platforms

- **Ubuntu**: ['focal', 'jammy']
- **Debian**: ['bullseye', 'bookworm']


#### Dependencies

No dependencies specified.
<!-- DOCSIBLE END -->
