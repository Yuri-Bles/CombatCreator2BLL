"""
Module Dockstring.
"""

import sys
import os
from typing import List, Any
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

    def get_stats_by_system_id(self, system_id: int, session: Session):
        """
        Method Docstring.
        """
        stats = session.query(DraftStat).filter(DraftStat.SystemID == system_id).all()
        return stats

    def update_system_stats_by_system_stat_id(self, system_id: int, session: Session, new_stat: List[Any]):
        """
        Method Docstring.
        """
        print(type(new_stat)) 
        print(new_stat.keys())
        print(new_stat['Id'])

        db_stat = session.query(DraftStat).filter_by(
            ID=new_stat['Id']
        ).first()

        print("Here")

        db_stat.name = new_stat['Name']
        db_stat.default_value = new_stat['DefaultValue']
        db_stat.min_value = new_stat['MinValue']
        db_stat.max_value = new_stat['MaxValue']

        session.commit()

stat_repository = StatRepository()