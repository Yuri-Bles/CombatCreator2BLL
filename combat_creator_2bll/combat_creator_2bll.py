"""
Docstring.
"""

from combat_system_draft import CombatSystemDraft
from combat_creator_3con.stat_repository import StatRepository


stat_repository = StatRepository()

new_combat_system = CombatSystemDraft(stat_repository, "Cool combat system", [
        ["Health Points", 18, 0, 20],
        ])

print(new_combat_system.get_all_stats())

new_combat_system.add_stat("Mana", 20, 0, None)

print(new_combat_system.get_all_stats())
