from enum import Enum
from src.core.attributes import Atbs, AtbsNames
from src.core.rolls import roll_basic_test
from dataclasses import dataclass
from src.core.enums.skills import SkillsName


@dataclass
class Skills:
    own:set[SkillsName]
    atbs: Atbs
    def roll(self, skill: SkillsName) -> int:
        if skill in self.own:
            return self.atbs.get_atb(skill.value).roll_with_prof()
        else:
            return self.atbs.get_atb(skill.value).roll()
