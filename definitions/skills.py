from enum import Enum
from definitions.attributes import Atbs, AtbsNames
from utils.rolls import roll_basic_test
from dataclasses import dataclass

class SkillsName(Enum):
  # Strength
  ATHLETICS = AtbsNames.STRENGTH
  # Dexterity
  ACROBATICS =  AtbsNames.DEXTERITY
  SLEIGHT_OF_HAND =  AtbsNames.DEXTERITY
  STEALTH =  AtbsNames.DEXTERITY
  # Intelligence
  ARCANA = AtbsNames.INTELLIGENCE
  HISTORY =  AtbsNames.INTELLIGENCE
  INVESTIGATION =  AtbsNames.INTELLIGENCE
  NATURE =  AtbsNames.INTELLIGENCE
  RELIGION =  AtbsNames.INTELLIGENCE
  # Wisdom
  ANIMAL_HANDLING =  AtbsNames.WISDOM
  INSIGHT =  AtbsNames.WISDOM
  MEDICINE =  AtbsNames.WISDOM
  PERCEPTION =  AtbsNames.WISDOM
  SURVIVAL =  AtbsNames.WISDOM
  # Charisma
  DECEPTION =  AtbsNames.CHARISMA
  INTIMIDATION =  AtbsNames.CHARISMA
  PERFORMANCE =  AtbsNames.CHARISMA
  PERSUASION =  AtbsNames.CHARISMA


@dataclass
class Skills:
    own:set[SkillsName]
    atbs: Atbs
    def roll(self, skill: SkillsName) -> int:
        if skill in self.own:
            return self.atbs.get_atb(skill.value).roll_with_prof()
        else:
            return self.atbs.get_atb(skill.value).roll()
