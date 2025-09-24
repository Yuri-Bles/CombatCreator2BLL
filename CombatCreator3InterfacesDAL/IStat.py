from abc import ABC, abstractmethod


class IStat(ABC):

    @abstractmethod
    def GetAllStatsByCombatSystemID(self, combatSystemID: int) -> list:
        pass