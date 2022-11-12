from dataclasses import dataclass, field
from random import choice
from typing import List

@dataclass
class Dice:
  value:int
  def roll(self):
    max = self.value
    return choice(range(1, max + 1))
  def __str__(self):
    return f'd{self.value}'

class Dices:
    def __init__(self, quant:int, dice:Dice, bonus:list[int] = []) -> None:
      self.dices = [dice for _ in range(quant)]
      self.bonus = bonus

    def roll(self):
        sum_results = sum(map(lambda d : d.roll(), self.dices))
        sum_bonus = sum(self.bonus)
        result = sum_results + sum_bonus
        return result

    def roll_vs(self, target:int) -> bool:
        return self.roll() >= target

# Lista de dados
d4 = Dice(4)
d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)
