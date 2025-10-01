"""
Docstring.
"""

from combat_system_draft import CombatSystemDraft # pylint: disable=E0401


new_combat_system = CombatSystemDraft("Cool combat system", [
        ["Health Points", 18, 0, 20],
        ])

print(new_combat_system.stats)

new_combat_system.add_stat("Mana", 20, 0, None)

print(new_combat_system.stats)
