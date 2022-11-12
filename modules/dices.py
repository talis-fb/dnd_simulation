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

@dataclass
class IDices:
  dices: List[Dice]
  bonus: List[int] = field(default_factory=list)

  def roll(self):
    sum_results = sum(map(lambda d : d.roll(), self.dices))
    sum_bonus = sum(self.bonus)
    result = sum_results + sum_bonus
    return result

  def __str__(self):
    return f'{len(self.dices)}d{self.dices[0]}'

# Lista de dados
d4 = Dice(4)
d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)

def gen_dice_list(quant: int, dice: List[Dice]):
  return [ dice for _ in range(quant) ]

def roll_dice(dice: Dice, bonus = 0):
  return dice.roll() + bonus

def roll_dices(dices: List[Dice], bonus = 0):
  results_each_dice = map(roll_dice, dices)
  result = sum(results_each_dice) + bonus
  return result

def roll_dices_vs(dices: List[Dice], target:int, bonus = 0):
  result = roll_dices(dices, bonus)
  return result >= target

def roll_test(target:int, bonus = 0):
  return d20.roll() + bonus

def roll_test_vs(target:int, bonus = 0):
  return (d20.roll() + bonus) >= target
