from typing import List
from utils.dices import Dice, d20

def roll_basic_test(bonus:list[int] = []):
  return d20.roll() + sum(bonus)

def roll_basic_test_vs(target:int, bonus:list[int] = []):
  return roll_basic_test(bonus) >= target
