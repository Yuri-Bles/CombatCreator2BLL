"""
Module docstring.
"""

from typing import List, Any
from combat_creator_3con.stat_interface import StatInterface
from sqlalchemy.orm import Session

class CombatSystemDraft:
    """Class docstring."""

    def __init__(self, _stat_repository: StatInterface, name: str, stats=None):
        """
        Method docstring.
        """
        self.stat_repository = _stat_repository
        self.name = name
        self.stats = []
        if stats is not None:
            for _stat in stats:
                self.add_stat(_stat[0], _stat[1], _stat[2], _stat[3])
        # The values of a stat are in order: Name, Default Value, Minimum Value, Maximum Value

    def add_stat(self, name: str, default_value: float, min_value: float, max_value: float):
        """
        Add a stat to the combat system.

        Args:
            name (str): Name of the stat.
            default_value (float): Default value of the stat.
            minimum_value (float): Minimum value allowed.
            maximum_value (float): Maximum value allowed.
        """
        self.stat_repository.add_stat(name, default_value, min_value, max_value)

    def create_system_stat(self, system_id: int, session: Session):
        """Creates a new stat"""
        stat = {}
        stat['Name'] = "New Stat"
        stat['DefaultValue'] = 75
        stat['MinValue'] = 0
        stat['MaxValue'] = 100
        self.stat_repository.create_system_stat(system_id, session, stat)

    def get_stats_by_system_id(self, system_id: int, session: Session):
        """Get all stats."""
        _stats = self.stat_repository.get_stats_by_system_id(system_id, session)
        result = []
        for stat in _stats:
            result.append([
                stat.ID,
                stat.name,
                float(stat.default_value),
                float(stat.min_value),
                float(stat.max_value)
            ])

        return result

    def update_system_stats_by_system_id(self, system_id: int, session: Session, stats: List[Any]):
        """Updates the stats on the page shown"""
        for stat in stats:
            if not (stat['MinValue'] < stat['DefaultValue'] < stat['MaxValue']):
                return jsonify({"error": "The minimum value must be lower than the default value, and the default value must be lower than the maximum value"}), 400
        for stat in stats:
            self.stat_repository.update_system_stats_by_system_stat_id(system_id, session, stat)

    def delete_system_stat(self, stat_id: int, session: Session):
        self.stat_repository.delete_system_stat(stat_id, session)

