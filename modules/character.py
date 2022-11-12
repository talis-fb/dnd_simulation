from enum import Enum
from dataclasses import dataclass, field
from typing import List,Set
from modules.dices import IDices, Dice, roll_test_vs
from modules.objects import Object
from modules.actions import Action

@dataclass
class CharacterSummary:
  name:str = ''
  race: str = ''
  classe:str = ''
  level:int = 1
  xp:int = 0

class Character(Object):
  def __init__(self, summary: CharacterSummary, atbs: Atbs, skills: Set[Skills] = {}, actions: List[Action] = []):
    self.atbs = atbs
    self.skills = skills
    self.summary = summary
    self.itens = []
    self.actions = actions

