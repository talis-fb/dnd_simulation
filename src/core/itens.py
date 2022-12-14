from abc import ABC, abstractmethod
from typing import List
from src.core.actions import Action

class Weapon(ABC):
    actions: List[Action]

    def get_actions(self):
        return self.actions

    def validate(self):
        pass
