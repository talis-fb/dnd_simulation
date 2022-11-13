from re import error
from definitions.actions import Action
from definitions.character import ICharacter
from utils.dices import d4, d6, d8, d10, d12, Dice, Dices
from typing import List

class IAttack_with_str_to_one_target(Action):
    damage_roll: Dices
    def run(self, attacker: ICharacter, defender: List[ICharacter]):
        if len(defender) > 1:
            raise error('Nao pode haver mais de um alvo nessa ação')
        roll = attacker.atbs.strength.roll_with_prof()
        target = defender[0].atbs.ac
        if roll >= target:
            damage = self.damage_roll.roll() + attacker.atbs.strength.value
            defender[0].atbs.hp -= damage


class Attack_with_dagger(IAttack_with_str_to_one_target):
    damage_roll = Dices(1, d4)

class Attack_with_handaxe(IAttack_with_str_to_one_target):
    damage_roll = Dices(1, d6)

