from typing import List
from src.core.actions import Action
from src.core.character import Character
from src.impl.actions.attacks.abstracts import Attack_one_target

class Multiple_attacks(Action):
    def __init__(self, attacks: List[Attack_one_target]) -> None:
        self.attacks = attacks

    def run(self, doing: Character, receiving: List[Character]):
        first = self.attacks[0]
        first.run(doing, receiving)

        successes = []
        results = []
        for move in self.attacks[1::]:
            move.with_disadvantage = True
            move.run(doing, receiving)
            results.append(move.result)
            successes.append(move.success)

        self.result = results
        self.success = all(successes)



