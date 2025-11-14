"""
Module Dockstring.
"""

import sys
import os
from sqlalchemy.orm import Session
from .models import DraftStat

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from combat_creator_3con.stat_interface import StatInterface

class StatRepository(StatInterface):
    """
    Class Docstring.
    """

    def add_stat(self, name: str, default_value: float, min_value: float, max_value: float):
        """
        Method Docstring.
        """

    def get_stats_by_system_id(self, session: Session):
        system_id = 1
        stats = session.query(DraftStat).filter(DraftStat.SystemID == system_id).all()
        return stats

stat_repository = StatRepository()