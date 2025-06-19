class CLIFlagBuilder:
    def __init__(self, flags, multiline=False, trailing_backslash=False):
        self.flags = flags or []
        self.multiline = multiline
        self.trailing_backslash = trailing_backslash

    def build(self):
        built_flags = []

        for item in self.flags:
            flag = self._build_flag(item)
            if flag:
                built_flags.extend(flag if isinstance(flag, list) else [flag])

        if not built_flags:
            return ""

        if self.multiline:
            if not self.trailing_backslash:
                built_flags[-1] = built_flags[-1].rstrip(" \\")
            return "\n".join(built_flags)
        else:
            return " ".join(f.rstrip(" \\") for f in built_flags)

    def _build_flag(self, item):
        if isinstance(item, dict):
            key = list(item.keys())[0]
            value = item[key]
            if value is None:
                return None

            if isinstance(value, bool):
                return [f"--{key}"] if value else None

            if isinstance(value, list):
                return [
                    f'--{key} "{val}" \\' if self.multiline else f'--{key} "{val}"'
                    for val in value
                ]

            return f'--{key} "{value}" \\' if self.multiline else f'--{key} "{value}"'

        elif isinstance(item, str):
            return f"--{item} \\" if self.multiline else f"--{item}"

        return None


class FilterModule:
    """
    Ansible filter plugin to convert a list of flags into a CLI-compatible string.
    """

    def filters(self):
        return {
            "to_cli_flags": self.to_cli_flags,
        }

    @staticmethod
    def to_cli_flags(flags, multiline=False, trailing_backslash=False):
        """
        Convert a list of CLI flags into a string for command-line usage.

        Args:
            flags (list): A list of strings or dicts representing CLI flags.
            multiline (bool): If True, output is multiline with backslashes.
            trailing_backslash (bool): If True, keep trailing backslash on last line.

        Returns:
            str: A CLI-ready string of flags.
        """
        return CLIFlagBuilder(flags, multiline, trailing_backslash).build()
