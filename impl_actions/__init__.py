from re import error
from definitions.actions import Action
from definitions.character import Character
from utils.dices import d4, d6, d8, d10, d12, Dice, Dices
from typing import List

class Attack_with_axe(Action):
    damage_roll = Dices(2, d6)
    def run(self, attacker: Character, defender: List[Character]):
        if len(defender) > 1:
            raise error('Nao pode haver mais de um alvo nessa ação')

        roll = attacker.atbs.strength.roll_with_prof()
        target = defender[0].atbs.ac
        if roll >= target:
            damage = self.damage_roll.roll()
            defender[0].atbs.hp -= damage
