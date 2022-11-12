from abc import ABC, abstractmethod
from typing import List
from definitions.character import Character
from random import choice

class Action(ABC):
  @property
  def is_able(self):
    return True

  @abstractmethod
  def run(self, doing: Character, receiving: List[Character]):
    pass

class Actions:
    def __init__(self, list_actions: List[Action]):
        self.current_action: Action | None = None
        self.actions = list_actions

    def set_randon_action(self):
        self.current_action = choice(self.actions)

    def exec(self, doing: Character, received: List[Character]):
        if self.current_action:
            self.current_action.run(doing, received)
