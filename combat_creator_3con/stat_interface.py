"""
Module Docstring.
"""

from abc import ABC, abstractmethod

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
    def remove_stat_by_name(self, name: str):
        """
        Method Docstring.
        """