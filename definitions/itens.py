from abc import ABC, abstractmethod
from typing import List
from definitions.actions import Action

class Weapon(ABC):
    actions: List[Action]

    def validate(self):
        pass
