from enum import Enum
from dataclasses import dataclass, field
from typing import List,Set
from modules.dices import IDices, Dice, roll_test_vs

class Atbs_Enum(Enum):
  STRENGTH = 'strength'
  DEXTERITY = 'dexterity'
  INTELLIGENCE = 'intelligence'
  WISDOM = 'wisdom'
  CHARISMA = 'charisma'

@dataclass
class Atbs:
  # As chaves aqui DEVEM ser iguais aos valores dos enums d cima
  strength:int
  dexterity:int
  intelligence:int
  wisdom:int
  charisma:int

  # Bonus
  prof_bonus:int = 2
  prof_atbs:Set[Atbs_Enum] = field(default_factory=set)

  # COMBAT
  ac:int = 15
  hp:int = 10
  hp_temp: List[int] = field(default_factory=int)
  hp_dice: List[IDices] = field(default_factory=Dice)

  def do_atb_test(self, atb: Atbs_Enum, target: int):
    bonus_in_test = self.__getattribute__(atb)

    if atb in self.prof_atbs:
      bonus_in_test += self.prof_bonus
    
    return roll_test_vs(target, bonus_in_test)

