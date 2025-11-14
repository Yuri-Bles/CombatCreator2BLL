"""
Module docstring.
"""

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

    def get_stats_by_system_id(self, session: Session):
        """Get all stats."""
        _stats = self.stat_repository.get_stats_by_system_id(session)
        result = [
            [stat.name, float(stat.default_value), float(stat.min_value), float(stat.max_value)]
            for stat in _stats
        ]
        return result
