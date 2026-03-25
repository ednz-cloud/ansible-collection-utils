class FilterModule:
    """
    Ansible filter plugin to render a dict as systemd unit file section lines.
    """

    def filters(self):
        return {
            "to_systemd_section": self.to_systemd_section,
        }

    @staticmethod
    def to_systemd_section(options):
        """
        Convert a dict of systemd unit options into key=value lines.

        List values produce one line per item (for directives that can appear
        multiple times, e.g. Volume=, WantedBy=, PublishPort=).
        Scalar values produce a single line.

        Args:
            options (dict): Mapping of systemd directive names to their values.

        Returns:
            str: Rendered lines ready to embed in a systemd unit section.
        """
        lines = []
        for key in sorted(options):
            value = options[key]
            if isinstance(value, list):
                for item in value:
                    lines.append(f"{key}={item}")
            else:
                lines.append(f"{key}={value}")
        return "\n".join(lines)
