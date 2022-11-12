from enum import Enum
from dataclasses import dataclass, field
from typing import List,Set
from modules.dices import IDices, Dice, roll_test_vs
from utils.rolls import roll_basic_test
from modules.skills import Skills

class AtbsNames(Enum):
  STRENGTH = 'strength'
  DEXTERITY = 'dexterity'
  INTELLIGENCE = 'intelligence'
  CONSTITUTION = 'constitution'
  WISDOM = 'wisdom'
  CHARISMA = 'charisma'

# Por padrão, vc pode iniciar Atb(5) com só o valor 
# ou com Atb(5,X), onde X seria o bonus de proficiencia,
# a existencia dele no parametro quer dizer que aquele atributo
# tem proficiencia
@dataclass
class Atb:
    value:int
    prof_bonus:int = 0
    def roll(self) -> int:
        return roll_basic_test([ self.value ])
    def roll_with_prof(self) -> int:
        return roll_basic_test([ self.value, self.prof_bonus ])


@dataclass
class Atbs:
  # As chaves aqui DEVEM ser iguais aos valores dos enums d cima
  strength: Atb
  dexterity:Atb
  intelligence:Atb
  constitution:Atb
  wisdom:Atb
  charisma:Atb
  def get_atb(self, atb:AtbsNames) -> Atb:
      return self.__getattribute__(str(atb))

  # Proficiencias
  prof_bonus:int = 2

  # COMBAT
  ac:int = 15
  hp:int = 10
  hp_temp: List[int] = field(default_factory=list)
  hp_dice: List[IDices] = field(default_factory=list)
