from CombatSystemDraft import CombatSystemDraft


newCombatSystem = CombatSystemDraft("Cool combat system", [
        ["Health Points", 18, 0, 20],
        ])

print(newCombatSystem.stats)

newCombatSystem.addStat("Mana", 20, 0, None)

print(newCombatSystem.stats)