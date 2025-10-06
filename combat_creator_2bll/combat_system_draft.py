"""
Module docstring.
"""

from stat_interface import StatInterface

class CombatSystemDraft:
    """Class docstring."""

    def __init__(self, _stat_repository: StatInterface, name: str, stats=None):
        """
        Method docstring.
        """
        self.stat_repository = _stat_repository
        self.name = name
        self.stats = stats if stats is not None else []
        for _stat in stats:
            self.add_stat(_stat[0], _stat[1], _stat[2], _stat[3])
        # The values of a stat are in order: Name, Default Value, Minimum Value, Maximum Value

    def add_stat(self, name: str, default_value: float, minimum_value: float, maximum_value: float):
        """
        Add a stat to the combat system.

        Args:
            name (str): Name of the stat.
            default_value (float): Default value of the stat.
            minimum_value (float): Minimum value allowed.
            maximum_value (float): Maximum value allowed.
        """
        self.stat_repository.add_stat(name, default_value, minimum_value, maximum_value)
        self.stats = self.get_all_stats

    def get_all_stats(self):
        """Get a stat by name."""
        return self.stat_repository.get_all_stats()
