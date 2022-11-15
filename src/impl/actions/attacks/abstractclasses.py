from re import error
from src.core.actions import Action
from src.core.attributes import AtbsNames as Atb_
from src.core.character import Character
from src.core.dices import Dices, d4, d6, d8, d10, d12
from typing import List

class IAttack_melee_to_one_target_without_prof(Action):
    damage_roll: Dices
    bonus_roll: int = 0
    bonus_damage: int = 0
    sum_with_strength:bool = True
    def run(self, attacker: Character, defender: List[Character]):
        if len(defender) > 1:
            raise error('Nao pode haver mais de um alvo nessa ação')

        roll = attacker.roll(Atb_.STRENGTH) + self.bonus_roll
        target = defender[0].heath.ac

        if roll >= target:
            damage = self.damage_roll.roll() + self.bonus_damage
            if self.sum_with_strength:
                damage += attacker.atbs.strength.value
            # defender[0].atbs.hp -= damage
            defender[0].heath.take_damage(damage)
            self.result = ((roll,target),damage)
            self.success = True
        else:
            self.result = (roll,target)
            self.success = False

class IAttack_melee_to_one_target_with_prof(Action):
    damage_roll: Dices
    bonus_roll: int = 0
    bonus_damage: int = 0
    sum_with_strength:bool = True
    def run(self, attacker: Character, defender: List[Character]):
        if len(defender) > 1:
            raise error('Nao pode haver mais de um alvo nessa ação')

        roll = attacker.roll_with_proficiency_bonus(Atb_.STRENGTH)
        roll += self.bonus_roll
        target = defender[0].heath.ac

        if roll >= target:
            damage = self.damage_roll.roll() + self.bonus_damage
            if self.sum_with_strength:
                damage += attacker.atbs.strength.value
            defender[0].heath.take_damage(damage)
            self.result = ((roll,target),damage)
            self.success = True
        else:
            self.result = (roll,target)
            self.success = False

