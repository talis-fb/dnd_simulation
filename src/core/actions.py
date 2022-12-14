from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Any

K = TypeVar('K')
class Action(ABC):
  is_able:bool = True

  result:Any = None
  success:bool = False

  @abstractmethod
  def run(self, doing: K, receiving: List[K]):
    pass

