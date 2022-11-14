from actions.interfaces.attacks import IAttack_melee_to_one_target_with_prof, IAttack_melee_to_one_target_without_prof
from utils.dices import Dices, d4, d6, d8, d10, d12

class Attack_with_dagger(IAttack_melee_to_one_target_without_prof):
    damage_roll = Dices(1, d4)

class Attack_with_handaxe(IAttack_melee_to_one_target_without_prof):
    damage_roll = Dices(1, d6)

class Attack_with_punch(IAttack_melee_to_one_target_with_prof):
    damage_roll = Dices(0, d6)
    bonus_damage = 1

class Attack_with_bite(IAttack_melee_to_one_target_with_prof):
    damage_roll = Dices(1, d4)

