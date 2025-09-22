from CombatSystemDraft import CombatSystemDraft


newCharacter = CombatSystemDraft([
        ["Health Points", 17, 0, 20],
        ])

print(newCharacter.stats)

newCharacter.addStat("Mana", 20, 0, None)

print(newCharacter.stats)