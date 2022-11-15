from src.core.dices import Dices, d4, d6, d8, d10, d12
from src.core.enums.types_damage import TypesDamage
from src.impl.itens.weapons.abstractclasses import MartialMeleeWeapon, MartialRangedWeapon, SimpleMeleeWeapon, SimpleRangedWeapon

# -------------------------------------------
# Simple ------------------------------------
# -------------------------------------------
class AdagaWithStrength(SimpleMeleeWeapon):
    damage_roll = Dices(1, d4)
    damage_type = TypesDamage.PIERCING

class AdagaWithDexterity(SimpleRangedWeapon): # Usado Ranged já que é por destreza
    damage_roll = Dices(1, d4)
    damage_type = TypesDamage.PIERCING

class Azagaia(SimpleMeleeWeapon):
    damage_roll = Dices(1, d6)
    damage_type = TypesDamage.PIERCING

class Lanca(SimpleMeleeWeapon):
    damage_roll = Dices(1, d6)
    damage_type = TypesDamage.PIERCING

class Machadinha(SimpleMeleeWeapon):
    damage_roll = Dices(1, d6)
    damage_type = TypesDamage.SLASHING

class MarteloLeve(SimpleMeleeWeapon):
    damage_roll = Dices(1, d4)
    damage_type = TypesDamage.BLUDGEONING

class ClavaGrande(SimpleMeleeWeapon):
    damage_roll = Dices(1, d8)
    damage_type = TypesDamage.BLUDGEONING

# -------------------------------------------
# Martial -----------------------------------
# -------------------------------------------
class CimitarraWithStrength(MartialMeleeWeapon):
    damage_roll = Dices(1, d6)
    damage_type = TypesDamage.SLASHING
class CimitarraWithDexterity(MartialRangedWeapon): # Usado Ranged já que é por destreza
    damage_roll = Dices(1, d6)
    damage_type = TypesDamage.SLASHING

class EspadaCurtaWithStrength(MartialMeleeWeapon):
    damage_roll = Dices(1, d6)
    damage_type = TypesDamage.PIERCING
class EspadaCurtaWithDexterity(MartialRangedWeapon):
    damage_roll = Dices(1, d6)
    damage_type = TypesDamage.PIERCING

class EspadaGrande(MartialMeleeWeapon):
    damage_roll = Dices(2, d6)
    damage_type = TypesDamage.SLASHING

class MachadoGrande(MartialMeleeWeapon):
    damage_roll = Dices(1, d12)
    damage_type = TypesDamage.SLASHING

class MachadoDeBatalha(MartialMeleeWeapon):
    damage_roll = Dices(1, d8)
    damage_type = TypesDamage.SLASHING
