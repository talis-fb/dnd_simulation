from src.core.enums.atbs import AtbsNames
from src.core.dices import Dices, d4
from src.core.enums.types_damage import TypesDamage
from src.impl.actions.attacks.abstracts import Attack_one_target

class Attack_Bite(Attack_one_target):
    damage_roll = Dices(1, d4)
    damage_type = TypesDamage.PIERCING
    atb = AtbsNames.STRENGTH
    sum_with_atb = AtbsNames.STRENGTH
