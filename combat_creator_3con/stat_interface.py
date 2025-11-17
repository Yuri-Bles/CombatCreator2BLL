"""
Module Docstring.
"""
from typing import List, Any
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

class StatInterface(ABC):
    """
    Class Docstring.
    """
    @abstractmethod
    def add_stat(self, name: str, default_value: float, min_value: float, max_value: float):
        """
        Method Docstring.
        """

    @abstractmethod
    def get_stats_by_system_id(self, system_id: int, session: Session):
        """
        Method Docstring.
        """

    @abstractmethod
    def update_system_stats_by_system_stat_id(self, system_id: int, session: Session, new_stat: List[Any]):
        """
        Method Docstring.
        """
