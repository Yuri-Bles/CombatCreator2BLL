"""
Module Docstring.
"""

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
    def get_stats_by_system_id(self, session: Session):
        """
        Method Docstring.
        """
