from core.dices import Dice, Dices
from core.enums.atbs import AtbsNames
from core.enums.types_damage import TypesDamage
from src.impl.actions.attacks.abstracts import Attack_one_target

class Attack_Punch(Attack_one_target):
    damage_roll = Dices(0, Dice(0))
    damage_type = TypesDamage.BLUDGEONING
    atb = AtbsNames.STRENGTH
    sum_with_atb = AtbsNames.STRENGTH
    bonus_damage = 1
