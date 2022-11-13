from dataclasses import dataclass, field
from enum import Enum
from typing import Set

class ProficienciesNames(Enum):
    WEAPON_SIMPLE = 'weapon_simple'
    WEAPON_MARTIAL = 'weapon_martial'
    LIGHT_ARMOR = 'light_armor'
    HEAVY_ARMOR = 'heavy_armor'

@dataclass
class Proficiencies:
    proficiencies: Set[ProficienciesNames] = field(default_factory=set)
    def contains(self, prof: ProficienciesNames):
        return prof in self.proficiencies
