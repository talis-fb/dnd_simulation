from src.core.dices import Dices, d6
from src.core.enums.proficiencies import ProficienciesNames
from src.core.itens import Weapon
from src.impl.actions.attacks.abstractclasses import (
    IAttack_melee_to_one_target_with_prof,
    IAttack_ranged_to_one_target_with_prof
)

class SimpleMeleeWeapon(IAttack_melee_to_one_target_with_prof):
    profiency = ProficienciesNames.WEAPON_SIMPLE

class SimpleRangedWeapon(IAttack_ranged_to_one_target_with_prof):
    profiency = ProficienciesNames.WEAPON_SIMPLE

class MartialMeleeWeapon(IAttack_melee_to_one_target_with_prof):
    profiency = ProficienciesNames.WEAPON_MARTIAL

class MartialRangedWeapon(IAttack_ranged_to_one_target_with_prof):
    profiency = ProficienciesNames.WEAPON_MARTIAL
