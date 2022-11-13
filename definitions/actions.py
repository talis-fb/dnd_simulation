from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

K = TypeVar('K')
class Action(ABC):
  @abstractmethod
  def run(self, doing: K, receiving: List[K]):
    pass

