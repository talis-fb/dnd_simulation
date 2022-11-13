from dataclasses import dataclass 
from typing import List,Set
from definitions.objects import Object
# from definitions.actions import Actions, Action
from definitions.skills import SkillsName, Skills
from definitions.attributes import Atbs
from abc import ABC, abstractmethod, abstractproperty
from random import choice

@dataclass
class CharacterSummary:
  name:str = ''
  race: str = ''
  classe:str = ''
  level:int = 1
  xp:int = 0

class ICharacter(ABC):
    @abstractproperty
    summary:CharacterSummary

class Action(ABC):
  @property
  def is_able(self):
    return True

  @abstractmethod
  def run(self, doing: ICharacter, receiving: List[ICharacter]):
    pass

class Character(ICharacter, Object):
  def __init__(self, summary: CharacterSummary, atbs: Atbs, skills: Set[SkillsName] = set(), actions: List[Action] = []):
    self.summary = summary
    self.atbs = atbs
    self.skills = Skills(skills, self.atbs)
    self.itens = []
    self.actions = actions
    self.current_action: Action | None = None

  def set_randon_action(self):
    self.current_action = choice(self.actions)

  def exec(self, doing: ICharacter, received: List[ICharacter]):
    if self.current_action:
      self.current_action.run(doing, received)

  #
  # class actions:
  #   def __init__(self, list_actions: List[Action]):
  #       self.current_action: Action | None = None
  #       self.actions = list_actions
  #
  #   def set_randon_action(self):
  #       self.current_action = choice(self.actions)
  #
  #   def exec(self, doing: ICharacter, received: List[ICharacter]):
  #       if self.current_action:
  #           self.current_action.run(doing, received)
  #
  #
