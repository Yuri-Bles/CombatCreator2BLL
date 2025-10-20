"""
Module Dockstring.
"""

import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from combat_creator_3con.stat_interface import StatInterface

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
