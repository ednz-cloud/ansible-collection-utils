from typing import List


class IniFileEntry:
    def __init__(self, section: str, option: str, value: str):
        self.section = section
        self.option = option
        self.value = value

    def to_dict(self):
        return {
            "section": self.section,
            "option": self.option,
            "value": self.value,
        }


class FilterModule(object):
    def filters(self):
        return {"to_ini_list": self.to_ini_list}

    def parse_ini_section(
        self, section_name: str, section_conf: dict
    ) -> List[IniFileEntry]:
        section_list = []
        for key, value in section_conf.items():
            if type(value) is dict:
                section_list.extend(
                    self.parse_ini_section(
                        section_name=f"{section_name}.{key}", section_conf=value
                    )
                )
            elif type(value) is list:
                section_list.append(
                    IniFileEntry(
                        section=section_name, option=key, value=",".join(value)
                    ).to_dict()
                )
            else:
                section_list.append(
                    IniFileEntry(
                        section=section_name, option=key, value=value
                    ).to_dict()
                )
        return section_list

    def to_ini_list(self, ini_file_dict: dict) -> List[IniFileEntry]:
        """
        Converts a nested dictionary structure into a flat list of dictionaries
        for use with the Ansible ini_file module.

        This function supports:
        - Nested sections: Nested dictionaries are processed recursively to produce
            hierarchical section names using dot notation (e.g., "section.subsection").
        - List values: Lists are converted into comma-separated strings, as INI files
            do not natively support lists.

        Example input:
            {
                "DEFAULT": {
                    "backend": "systemd",
                    "username": "openstack",
                    "nested": {
                        "suboption": "value",
                        "another": ["list", "of", "values"]
                    }
                }
            }

        Output:
            [
                {"section": "DEFAULT", "option": "backend", "value": "systemd"},
                {"section": "DEFAULT", "option": "username", "value": "openstack"},
                {"section": "DEFAULT.nested", "option": "suboption", "value": "value"},
                {"section": "DEFAULT.nested", "option": "another", "value": "list,of,values"}
            ]

        Args:
            ini_file_dict (dict): A dictionary representing INI configuration,
                where the top-level keys are sections and the values are key-value
                pairs or nested dictionaries.

        Returns:
            List[Dict[str, str]]: A flat list of dictionaries with keys "section",
                "option", and "value", suitable for consumption by the ini_file module.
        """
        result = []
        for section, options in ini_file_dict.items():
            result.extend(
                self.parse_ini_section(section_name=section, section_conf=options)
            )
        return result
