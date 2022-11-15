from dataclasses import dataclass, field
from enum import Enum
from typing import Set
from src.core.enums.proficiencies import ProficienciesNames

@dataclass
class Proficiencies:
    proficiencies: Set[ProficienciesNames] = field(default_factory=set)
    def contains(self, prof: ProficienciesNames):
        return prof in self.proficiencies
