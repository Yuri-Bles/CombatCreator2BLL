"""
Module Dockstring.
"""

from stat_interface import StatInterface

class StatRepository(StatInterface):
    """
    Class Docstring.
    """
    stats = []

    def add_stat(self, name: str, default_value: float, min_value: float, max_value: float):
        """
        Method Docstring.
        """
        self.stats.append([name, default_value, min_value, max_value])

    def get_all_stats(self):
        """
        Method Docstring.
        """
        return self.stats
