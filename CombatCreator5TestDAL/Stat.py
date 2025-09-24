from CombatCreator3InterfacesDAL.IStat import IStat


class StatTestRepository(IStat):
    def __init__(self):
        pass

    def GetAllStatsByCombatSystemID(self, combatSystemID: int) -> list:
        return list([["Health Points", 17, 0, 20], ["Mana", 10, 0, 40]])