from dataclasses import dataclass 
from typing import List,Set
from definitions.objects import Object
from definitions.actions import Action
from definitions.skills import SkillsName, Skills
from definitions.attributes import Atbs

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

