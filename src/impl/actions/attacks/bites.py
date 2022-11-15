from src.core.dices import Dices, d4
from src.core.enums.types_damage import TypesDamage
from src.impl.actions.attacks.abstractclasses import IAttack_melee_to_one_target_with_prof_bonus

class Attack_Bite(IAttack_melee_to_one_target_with_prof_bonus):
    damage_roll = Dices(1, d4)
    damage_type = TypesDamage.PIERCING
