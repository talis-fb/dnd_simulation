from src.core.enums.atbs import AtbsNames
from src.core.enums.types_damage import TypesDamage
from src.core.dices import Dices, d6
from src.core.enums.proficiencies import ProficienciesNames
from src.core.itens import Weapon
from src.impl.actions.attacks.abstracts import Attack_one_target



class SimpleMeleeWeapon(Attack_one_target):
    atb = AtbsNames.STRENGTH
    with_profiency = ProficienciesNames.WEAPON_SIMPLE

class SimpleRangedWeapon(Attack_one_target):
    atb = AtbsNames.DEXTERITY
    with_profiency = ProficienciesNames.WEAPON_SIMPLE

class MartialMeleeWeapon(Attack_one_target):
    atb = AtbsNames.STRENGTH
    with_profiency = ProficienciesNames.WEAPON_MARTIAL

class MartialRangedWeapon(Attack_one_target):
    atb = AtbsNames.DEXTERITY
    with_profiency = ProficienciesNames.WEAPON_MARTIAL
