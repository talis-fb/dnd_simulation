from dataclasses import dataclass,field
from src.core.enums.types_damage import TypesDamage
from src.core.enums.conditions import Conditions
from typing import Set

@dataclass
class Object:
  resistance: Set[TypesDamage] = field(default_factory=set)
  vulnerability:Set[TypesDamage] = field(default_factory=set)
  invisible: Set[TypesDamage] = field(default_factory=set)
  conditions: Set[Conditions] = field(default_factory=set)
