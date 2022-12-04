from typing import List
from src.core.actions import Action
from src.core.character import Character
from src.impl.actions.attacks.abstracts import Attack_one_target

class Multiple_attacks(Action):
    def __init__(self, attacks: List[Attack_one_target], attacks_with_disadvantage: List[Attack_one_target] = []) -> None:
        self.attacks = attacks
        self.attacks_with_disadvantage = attacks_with_disadvantage

    def run(self, doing: Character, receiving: List[Character]):
        successes = []
        results = []

        for attack in self.attacks:
            attack.run(doing, receiving)
            results.append(attack.result)
            successes.append(attack.success)

        for attack in self.attacks_with_disadvantage:
            attack.with_disadvantage = True
            attack.run(doing, receiving)
            results.append(attack.result)
            successes.append(attack.success)

        self.result = results
        self.success = all(successes)



