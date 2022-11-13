from abc import ABC, abstractmethod
from typing import List
from definitions.character import ICharacter
from random import choice

class Action(ABC):
  @property
  def is_able(self):
    return True

  @abstractmethod
  def run(self, doing: ICharacter, receiving: List[ICharacter]):
    pass
