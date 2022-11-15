from src.core.dices import Dices, d4, d6, d8, d10, d12
from src.core.enums.types_damage import TypesDamage
from src.impl.itens.weapons.abstractclasses import MartialRangedWeapon, SimpleRangedWeapon

# Simple -----------------------------------
class ArcoCurto(SimpleRangedWeapon):
    damage_roll = Dices(1, d6)
    damage_type = TypesDamage.PIERCING

class BestaLeve(SimpleRangedWeapon):
    damage_roll = Dices(1, d8)
    damage_type = TypesDamage.PIERCING

class Dardo(SimpleRangedWeapon):
    damage_roll = Dices(1, d4)
    damage_type = TypesDamage.PIERCING

class Funda(SimpleRangedWeapon):
    damage_roll = Dices(1, d4)
    damage_type = TypesDamage.BLUDGEONING

# Martial -----------------------------------
class ArcoLongo(MartialRangedWeapon):
    damage_roll = Dices(1, d8)
    damage_type = TypesDamage.PIERCING

class BestaDeMao(MartialRangedWeapon):
    damage_roll = Dices(1, d6)
    damage_type = TypesDamage.PIERCING

class BestaPesada(MartialRangedWeapon):
    damage_roll = Dices(1, d10)
    damage_type = TypesDamage.PIERCING
