class CombatSystemDraft:
    def __init__(self, stats):
        self.stats = stats

        #The values of a stat are in order: Name, Default Value, Minimum Value, Maximum Value
    stats = list([])

    def addStat(self, name: str, defaultValue: int, minimumValue: int, maximumValue: int):
        self.stats.append([name, defaultValue, minimumValue, maximumValue])




