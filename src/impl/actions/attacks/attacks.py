from src.impl.actions.attacks.abstractclasses import (
    IAttack_melee_to_one_target_with_prof_bonus, 
    IAttack_melee_to_one_target_without_prof_bonus
)
from src.core.dices import Dices, d4, d6, d8, d10, d12

# class Attack_with_

class Attack_with_dagger(IAttack_melee_to_one_target_without_prof_bonus):
    damage_roll = Dices(1, d4)

class Attack_with_handaxe(IAttack_melee_to_one_target_without_prof_bonus):
    damage_roll = Dices(1, d6)

class Attack_with_punch(IAttack_melee_to_one_target_with_prof_bonus):
    damage_roll = Dices(0, d6)
    sum_with_strength = True
    bonus_damage = 1

class Attack_with_bite(IAttack_melee_to_one_target_with_prof_bonus):
    damage_roll = Dices(1, d4)

