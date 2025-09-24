from asyncio.windows_events import NULL


class CombatSystemDraft:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

        #The values of a stat are in order: Name, Default Value, Minimum Value, Maximum Value
    
    name = NULL
    stats = list([])

    def addStat(self, name: str, defaultValue: int, minimumValue: int, maximumValue: int):
        self.stats.append([name, defaultValue, minimumValue, maximumValue])