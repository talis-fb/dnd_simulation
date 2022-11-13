from dataclasses import dataclass
from typing import Generic, List,Set,TypeVar
from typing_extensions import Self
from definitions.objects import Object
from definitions.actions import Action
from definitions.skills import SkillsName, Skills
from definitions.attributes import Atbs
from abc import ABC, abstractmethod 
from random import choice

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
    self.current_action: Action | None = None

  def set_randon_action(self):
    self.current_action = choice(self.actions)

  def exec(self, received: List[Self]):
    if self.current_action:
      self.current_action.run(self, received)

