from dataclasses import dataclass
from typing import Generic, List,Set,TypeVar
from typing_extensions import Self
from src.core.objects import Object
from src.core.actions import Action
from src.core.skills import SkillsName, Skills
from src.core.attributes import Atbs, AtbsNames
from abc import ABC, abstractmethod 
from random import choice
from src.core.proficiencies import Proficiencies, ProficienciesNames
from src.core.combat_stats import Heath

@dataclass
class CharacterSummary:
  name:str = ''
  race: str = ''
  classe:str = ''
  level:int = 1
  xp:int = 0

class Character(Object):
  def __init__(self, summary: CharacterSummary, atbs: Atbs, heath: Heath, skills: Set[SkillsName] = set(), actions: List[Action] = []):
    self.summary = summary
    self.atbs = atbs
    self.heath = heath
    self.skills = Skills(skills, self.atbs)
    self.itens = []
    self.actions = actions
    self.current_action: Action
    self.proficiencies = Proficiencies(set())

  ## Rolls ------------------------------------
  def roll(self, atb: AtbsNames):
      return self.atbs.roll(atb)

  def roll_with_proficiency(self, atb: AtbsNames, prof: ProficienciesNames, advantage:bool = False, disadvantage:bool = False):
      roll_result = self.atbs.roll(atb, advantage=advantage, disadvantage=disadvantage)
      if self.proficiencies.contains(prof):
          return roll_result + self.atbs.proficiency_bonus
      else:
          return roll_result

  def roll_with_proficiency_bonus(self, atb: AtbsNames, advantage = False, disadvantage = False):
      roll_result = self.atbs.roll(atb, advantage=advantage, disadvantage=disadvantage)
      return roll_result + self.atbs.proficiency_bonus

  def roll_saving_throw(self, atb:AtbsNames, advantage = False, disadvantage = False):
      roll_result = self.atbs.roll(atb, advantage=advantage, disadvantage=disadvantage)
      if self.atbs.is_in_saving_throw(atb):
          return roll_result + self.atbs.proficiency_bonus
      else:
          return roll_result

  def roll_with_bonus(self, atb:AtbsNames, bonus:int, advantage = False, disadvantage = False):
      roll_result = self.atbs.roll(atb, advantage=advantage, disadvantage=disadvantage)
      return roll_result + bonus

  ## Manage ACTIONS ---------------------------
  def set_randon_action(self):
    choiced = choice(self.actions)

    # Vai escolhendo ate achar uma ação permitida
    # TODO: NADA perfomatico
    while not choiced.is_able:
       choiced = choice(self.actions)

    self.current_action = choice(self.actions)

  def exec(self, received: List[Self]):
    if self.current_action:
      return self.current_action.run(self, received)

