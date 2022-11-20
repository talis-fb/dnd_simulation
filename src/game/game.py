from typing import Any, Callable
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
        self.attacker = factory_character1()
        self.defender = factory_character2()
        logging.basicConfig(filename=f'{log_file}.txt')

        self.turn = 0
        self.diff_hp = 0
        self.winner: Character | None = None
        self.results:Any = None
        self.last_roll:bool = False

    def restart_game(self):
        self.attacker = self.factory_character1()
        self.defender = self.factory_character2()

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
        self.diff_hp =self.attacker.heath.hp - self.defender.heath.hp

        return {
            "winner": self.winner.summary.name,
            "dif_hp": self.diff_hp
        }

    def next_turn(self):
        self.attacker, self.defender = self.defender, self.attacker
        self.turn += 1

    def validate_turn(self):
        # self.attacker.validate_actions()
        # self.defender.validate_actions()
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
