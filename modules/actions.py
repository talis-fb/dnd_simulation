from abc import ABC, abstractmethod
from modules.character import Character

class Action(ABC):
  @property
  def is_able(self):
    return True

  @abstractmethod
  def run(self, doing: Character, receiving: Character):
    pass
