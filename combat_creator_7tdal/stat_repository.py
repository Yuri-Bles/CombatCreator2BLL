"""
Module Dockstring.
"""

import sys
import os
from sqlalchemy.orm import Session

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from combat_creator_3con.stat_interface import StatInterface

class StatRepository(StatInterface):
    """
    Class Docstring.
    """
    stats = [
        ["HP", 34, 0, 42],
        ["Mana", 25, 0, 50]
    ]

    def create_system_stat(self, system_id: int, session: Session, new_stat: List[Any]):
        """
        Method Docstring.
        """
        self.stats.append([name, default_value, min_value, max_value])

    def get_stats_by_system_id(self, system_id: int, session: Session):
        """
        Method Docstring.
        """
        return self.stats

    def update_system_stats_by_system_stat_id(self, system_id: int, session: Session), new_stat: List[Any]:
        """
        Method Docstring.
        """

    def delete_system_stat(self, stat_id: int, session: Session):
        """
        Method Docstring.
        """

stat_repository = StatRepository()