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
    def get_all_stats(self):
        """
        Method Docstring.
        """
