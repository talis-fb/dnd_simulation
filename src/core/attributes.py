from enum import Enum
from dataclasses import dataclass, field
from typing import List,Set
from src.core.dices import Dices
from src.core.rolls import roll_basic_test
from src.core.proficiencies import Proficiencies
from src.core.enums.atbs import AtbsNames

# Por padrão, vc pode iniciar Atb(5) com só o valor 
# ou com Atb(5,X), onde X seria o bonus de proficiencia,
# a existencia dele no parametro quer dizer que aquele atributo
# tem proficiencia
@dataclass
class Atb:
    value:int
    def roll(self, advantage:bool = False, disadvantage:bool = False) -> int:
        if advantage and disadvantage:
            raise Exception('Advantage + Disadvantage together in a roll')
        if advantage:
            return self.roll_with_advantage()
        if disadvantage:
            return self.roll_with_disadvantage()

        return roll_basic_test([ self.value ])

    def roll_with_bonus(self, bonus:int) -> int:
        return roll_basic_test([ self.value, bonus ])

    # Advantage / Disadvantage
    def roll_with_advantage(self) -> int:
        both_rolls = [ roll_basic_test([ self.value ]), roll_basic_test([ self.value ]) ]
        return max(both_rolls)
    def roll_with_disadvantage(self) -> int:
        both_rolls = [ roll_basic_test([ self.value ]), roll_basic_test([ self.value ]) ]
        return min(both_rolls)

    # Clone the instance of class
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
      return self.__getattribute__(str(atb.value))

  def roll(self, atb:AtbsNames, advantage=False, disadvantage=False) -> int:
      return self.get_atb(atb).roll(advantage=advantage, disadvantage=disadvantage)

  def is_in_saving_throw(self, atb:AtbsNames) -> bool:
      return atb in self.saving_throws
