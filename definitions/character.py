from dataclasses import dataclass
from typing import Generic, List,Set,TypeVar
from typing_extensions import Self
from definitions.objects import Object
from definitions.actions import Action
from definitions.skills import SkillsName, Skills
from definitions.attributes import Atbs, AtbsNames
from abc import ABC, abstractmethod 
from random import choice
from definitions.proficiencies import Proficiencies, ProficienciesNames

@dataclass
class CharacterSummary:
  name:str = ''
  race: str = ''
  classe:str = ''
  level:int = 1
  xp:int = 0

class Character(Object):
  def __init__(self, summary: CharacterSummary, atbs: Atbs, skills: Set[SkillsName] = set(), actions: List[Action] = []):
    self.summary = summary
    self.atbs = atbs
    self.skills = Skills(skills, self.atbs)
    self.itens = []
    self.actions = actions
    self.current_action: Action
    self.proficiencies = Proficiencies(set())

  ## Rolls ------------------------------------
  def roll(self, atb: AtbsNames):
      return self.atbs.roll(atb)

  def roll_with_proficiency(self, atb: AtbsNames, prof: ProficienciesNames):
      roll_result = self.atbs.roll(atb)
      if self.proficiencies.contains(prof):
          return roll_result + self.atbs.proficiency_bonus
      else:
          return roll_result

  def roll_with_proficiency_bonus(self, atb: AtbsNames):
      roll_result = self.atbs.roll(atb)
      return roll_result + self.atbs.proficiency_bonus

  def roll_saving_throw(self, atb:AtbsNames):
      roll_result = self.atbs.roll(atb)
      if self.atbs.is_in_saving_throw(atb):
          return roll_result + self.atbs.proficiency_bonus
      else:
          return roll_result

  def roll_with_bonus(self, atb:AtbsNames, bonus:int):
      roll_result = self.atbs.roll(atb)
      return roll_result + bonus

  ## Manage ACTIONS ---------------------------
  def set_randon_action(self):
    self.current_action = choice(self.actions)

  def exec(self, received: List[Self]):
    if self.current_action:
      return self.current_action.run(self, received)

