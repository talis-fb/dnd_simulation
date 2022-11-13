from enum import Enum
from dataclasses import dataclass, field
from typing import List,Set
from utils.dices import Dices
from utils.rolls import roll_basic_test
# from definitions.skills import Skills
from definitions.proficiencies import Proficiencies

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
    def roll(self) -> int:
        return roll_basic_test([ self.value ])
    def roll_with_bonus(self, bonus:int) -> int:
        return roll_basic_test([ self.value, bonus ])
    def clone_with_bonus(self, bonus: int):
        return Atb(self.value + bonus)


@dataclass
class Atbs:
  # As chaves aqui DEVEM ser iguais aos valores dos enums d cima
  strength: Atb
  dexterity:Atb
  intelligence:Atb
  constitution:Atb
  wisdom:Atb
  charisma:Atb
  proficiency_bonus:int
  saving_throws: Set[AtbsNames] = field(default_factory=set)

  def get_atb(self, atb:AtbsNames) -> Atb:
      return self.__getattribute__(str(atb))

  def roll(self, atb:AtbsNames) -> int:
      return self.get_atb(atb).roll()

  def is_in_saving_throw(self, atb:AtbsNames) -> bool:
      return atb in self.saving_throws

  # def clone_with_bonus(self, bonus: int):
  #     return Atbs(
  #         strength=self.strength.clone_with_bonus(bonus),
  #         dexterity=self.dexterity.clone_with_bonus(bonus),
  #         intelligence=self.intelligence.clone_with_bonus(bonus),
  #         constitution=self.constitution.clone_with_bonus(bonus),
  #         wisdom=self.wisdom.clone_with_bonus(bonus),
  #         charisma=self.charisma.clone_with_bonus(bonus)
  #     )

  # COMBAT
  ac:int = 15
  hp:int = 10
  hp_temp: List[int] = field(default_factory=list)
  hp_dice: Dices | None = None
