from re import error
from src.core.enums.types_damage import TypesDamage
from src.core.actions import Action
from src.core.attributes import AtbsNames as Atb_
from src.core.character import Character
from src.core.dices import Dices, d4, d6, d8, d10, d12
from src.core.enums.proficiencies import ProficienciesNames
from typing import List
from abc import ABC, abstractmethod

## -------------
## INTERFACES
## -------------
class IAttack(Action, ABC):
    damage_roll: Dices
    bonus_roll: int = 0
    bonus_damage: int = 0
    damage_type: TypesDamage | None = None
    sum_with_strength:bool = True
    
    with_advantage:bool = False
    with_disadvantage:bool = False
    
    @abstractmethod
    def run(self, attacker: Character, defender: List[Character]):
        pass

# Melee---------------
class IAttack_melee_to_one_target_without_prof_bonus(IAttack):
    def run(self, attacker: Character, defender: List[Character]):
        if len(defender) > 1:
            raise error('Nao pode haver mais de um alvo nessa ação')

        roll = attacker.roll(
            Atb_.STRENGTH, 
            advantage=self.with_advantage,
            disadvantage=self.with_disadvantage,
        )
        roll += self.bonus_roll
        
        hit = defender[0].heath.is_ac_less_than(roll)
        
        if hit:
            damage = self.damage_roll.roll() + self.bonus_damage
            if self.sum_with_strength:
                damage += attacker.atbs.strength.value
            defender[0].heath.take_damage(damage, self.damage_type)
            self.result = ((roll,defender[0].heath.ac),damage)
            self.success = True
        else:
            self.result = ((roll,defender[0].heath.ac))
            self.success = False

class IAttack_melee_to_one_target_with_prof_bonus(IAttack):
    def run(self, attacker: Character, defender: List[Character]):
        if len(defender) > 1:
            raise error('Nao pode haver mais de um alvo nessa ação')

        roll = attacker.roll_with_proficiency_bonus(
            Atb_.STRENGTH, 
            advantage=self.with_advantage,
            disadvantage=self.with_disadvantage,
        )
        roll += self.bonus_roll
        
        hit = defender[0].heath.is_ac_less_than(roll)
        
        if hit:
            damage = self.damage_roll.roll() + self.bonus_damage
            if self.sum_with_strength:
                damage += attacker.atbs.strength.value
            defender[0].heath.take_damage(damage, self.damage_type)
            self.result = ((roll,defender[0].heath.ac),damage)
            self.success = True
        else:
            self.result = ((roll,defender[0].heath.ac))
            self.success = False

class IAttack_melee_to_one_target_with_prof(IAttack):
    profiency: ProficienciesNames
    def run(self, attacker: Character, defender: List[Character]):
        if len(defender) > 1:
            raise error('Nao pode haver mais de um alvo nessa ação')

        roll = attacker.roll_with_proficiency(
            Atb_.STRENGTH, 
            self.profiency,
            advantage=self.with_advantage,
            disadvantage=self.with_disadvantage,
        )
        roll += self.bonus_roll
        
        hit = defender[0].heath.is_ac_less_than(roll)
        
        if hit:
            damage = self.damage_roll.roll() + self.bonus_damage
            if self.sum_with_strength:
                damage += attacker.atbs.strength.value
            defender[0].heath.take_damage(damage, self.damage_type)
            self.result = ((roll,defender[0].heath.ac),damage)
            self.success = True
        else:
            self.result = ((roll,defender[0].heath.ac))
            self.success = False


# RANGED---------------
class IAttack_ranged_to_one_target_without_prof_bonus(IAttack):
    def run(self, attacker: Character, defender: List[Character]):
        if len(defender) > 1:
            raise error('Nao pode haver mais de um alvo nessa ação')

        roll = attacker.roll(
            Atb_.DEXTERITY, 
            advantage=self.with_advantage,
            disadvantage=self.with_disadvantage,
        )
        roll += self.bonus_roll
        
        hit = defender[0].heath.is_ac_less_than(roll)
        
        if hit:
            damage = self.damage_roll.roll() + self.bonus_damage
            if self.sum_with_strength:
                damage += attacker.atbs.strength.value
            defender[0].heath.take_damage(damage, self.damage_type)
            self.result = ((roll,defender[0].heath.ac),damage)
            self.success = True
        else:
            self.result = ((roll,defender[0].heath.ac))
            self.success = False

class IAttack_ranged_to_one_target_with_prof_bonus(IAttack):
    def run(self, attacker: Character, defender: List[Character]):
        if len(defender) > 1:
            raise error('Nao pode haver mais de um alvo nessa ação')

        roll = attacker.roll_with_proficiency_bonus(
            Atb_.DEXTERITY, 
            advantage=self.with_advantage,
            disadvantage=self.with_disadvantage,
        )
        roll += self.bonus_roll
        
        hit = defender[0].heath.is_ac_less_than(roll)
        
        if hit:
            damage = self.damage_roll.roll() + self.bonus_damage
            if self.sum_with_strength:
                damage += attacker.atbs.strength.value
            defender[0].heath.take_damage(damage, self.damage_type)
            self.result = ((roll,defender[0].heath.ac),damage)
            self.success = True
        else:
            self.result = ((roll,defender[0].heath.ac))
            self.success = False

class IAttack_ranged_to_one_target_with_prof(IAttack):
    profiency: ProficienciesNames
    def run(self, attacker: Character, defender: List[Character]):
        if len(defender) > 1:
            raise error('Nao pode haver mais de um alvo nessa ação')

        roll = attacker.roll_with_proficiency(
            Atb_.DEXTERITY, 
            self.profiency,
            advantage=self.with_advantage,
            disadvantage=self.with_disadvantage,
        )
        roll += self.bonus_roll
        
        hit = defender[0].heath.is_ac_less_than(roll)
        
        if hit:
            damage = self.damage_roll.roll() + self.bonus_damage
            if self.sum_with_strength:
                damage += attacker.atbs.strength.value
            defender[0].heath.take_damage(damage, self.damage_type)
            self.result = ((roll,defender[0].heath.ac),damage)
            self.success = True
        else:
            self.result = ((roll,defender[0].heath.ac))
            self.success = False

