class FilterModule(object):
    """
    Ansible filter plugin for checking item change status in results.
    """

    def filters(self):
        return {"item_changed_in_list": self.item_changed_in_list}

    @staticmethod
    def item_changed_in_list(results, item):
        """
        Check if a specific item in the results list has the `changed` attribute set to True.

        Args:
            results (list): The list of result dictionaries from a task.
            item (str): The item name to search for.

        Returns:
            bool: True if the `changed` attribute is True for the specified item, False otherwise.
        """
        if not isinstance(results, list):
            raise ValueError("The 'results' argument must be a list.")
        if not isinstance(item, str):
            raise ValueError("The 'item' argument must be a string.")

        for result in results:
            if result.get("item") == item:
                return result.get("changed", False)
        return False
