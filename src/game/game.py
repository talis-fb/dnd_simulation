from typing import Any, Callable, Literal
from dataclasses import dataclass
from src.core.character import Character
import logging

class Game:
    def __init__(
        self,
        factory_character1: Callable[..., Character],
        factory_character2: Callable[..., Character],
        log_file:str = "results"
    ) -> None:
        self.factory_character1 = factory_character1
        self.factory_character2 = factory_character2
        self.characters = (
            factory_character1(),
            factory_character2(),
        )
        self.current_character:int = 0

        logging.basicConfig(filename=f'{log_file}.txt')

        self.turn = 0
        self.diff_hp = 0
        self.winner: Character | None = None
        self.results:Any = None
        self.last_roll:bool = False

    @property
    def attacker(self):
        return self.characters[self.current_character]

    @property
    def defender(self):
        i = int(not self.current_character)
        return self.characters[i]

    def restart_game(self):
        self.characters = (
            self.factory_character1(),
            self.factory_character2()
        )
        self.current_character = 0

    @property
    def is_finished(self) -> bool:
        return (
            self.attacker.heath.is_dead() or
            self.defender.heath.is_dead()
        )
    def get_game_results(self):
        if self.attacker.heath.hp > self.defender.heath.hp:
            self.winner = self.attacker
        else:
            self.winner = self.defender
        self.diff_hp = max([ self.attacker.heath.hp, 0 ]) - max([self.defender.heath.hp, 0])

        return {
            "winner": self.winner.summary.name,
            "diff_hp": self.diff_hp
        }

    def next_turn(self):
        self.current_character += 1

        # Se estourar
        if self.current_character >= len(self.characters):
            self.current_character = 0

        self.turn += 1

    def validate_turn(self):
        self.attacker.set_randon_action()

    def run_turn(self):
        self.attacker.exec([ self.defender ])

    def log_turn_results(self):
        self.last_roll = self.attacker.current_action.success
        self.results = self.attacker.current_action.result
        # logging.info(f'{self.last_roll} => {self.results}   ||   {self.get_game_results()}')
        pass

    def log_game_results(self):
        pass
