from core.dices import Dice, Dices, d4
from core.enums.types_damage import TypesDamage
from src.impl.actions.attacks.abstractclasses import IAttack_melee_to_one_target_with_prof_bonus

class Attack_Punch(IAttack_melee_to_one_target_with_prof_bonus):
    damage_type = TypesDamage.BLUDGEONING
    damage_roll = Dices(0, Dice(0))
    sum_with_strength = True
    bonus_damage = 1
