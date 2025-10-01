"""
Module docstring.
"""

class CombatSystemDraft:
    """Class docstring."""

    def __init__(self, name: str, stats=None):
        """
        Method docstring.
        """
        self.name = name
        self.stats = stats if stats is not None else []
        # The values of a stat are in order: Name, Default Value, Minimum Value, Maximum Value

    def add_stat(self, name: str, default_value: int, minimum_value: int, maximum_value: int):
        """
        Add a stat to the combat system.

        Args:
            name (str): Name of the stat.
            default_value (int): Default value of the stat.
            minimum_value (int): Minimum allowable value.
            maximum_value (int): Maximum allowable value.
        """
        self.stats.append([name, default_value, minimum_value, maximum_value])

    def remove_stat(self, name: str):
        """Remove a stat by name."""
        for stat in self.stats:
            if stat[0] == name:
                self.stats.remove(stat)
