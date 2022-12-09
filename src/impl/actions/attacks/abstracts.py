from dataclasses import dataclass
from re import error
from src.core.enums.atbs import AtbsNames
from src.core.enums.types_damage import TypesDamage
from src.core.actions import Action
from src.core.attributes import AtbsNames
from src.core.character import Character
from src.core.dices import Dice, Dices
from src.core.enums.proficiencies import ProficienciesNames
from typing import List

## -------------
## INTERFACES
## -------------
class Attack_one_target(Action):
    damage_roll: Dices
    damage_type: TypesDamage | None = None
    atb: AtbsNames = AtbsNames.STRENGTH
    sum_with_atb:AtbsNames | None = AtbsNames.STRENGTH
    bonus_roll: int = 0
    bonus_damage: int = 0

    with_profiency: ProficienciesNames | None = None
    with_profiency_bonus: bool = False
    with_advantage:bool = False
    with_disadvantage:bool = False

    def run(self, attacker: Character, defender: List[Character]):
        if len(defender) > 1:
            raise error('Nao pode haver mais de um alvo nessa ação')

        if self.with_profiency_bonus:
            roll = attacker.roll_with_proficiency_bonus(
                self.atb,
                advantage=self.with_advantage,
                disadvantage=self.with_disadvantage,
            )
        elif self.with_profiency:
            roll = attacker.roll_with_proficiency(
                self.atb,
                prof=self.with_profiency,
                advantage=self.with_advantage,
                disadvantage=self.with_disadvantage,
            )
        else:
            roll = attacker.roll(
                self.atb,
                advantage=self.with_advantage,
                disadvantage=self.with_disadvantage,
            )

        roll += self.bonus_roll
        hit = defender[0].heath.is_ac_less_than(roll)
        
        if hit:
            damage = self.damage_roll.roll() + self.bonus_damage

            if self.sum_with_atb:
                damage += attacker.atbs.get_atb(self.sum_with_atb).value

            defender[0].heath.take_damage(damage, self.damage_type)
            self.result = ((roll,defender[0].heath.ac),damage)
            self.success = True
        else:
            self.result = ((roll,defender[0].heath.ac))
            self.success = False


class Attack_one_target_with_saving_throw(Attack_one_target):
    atb_saving_throw: AtbsNames
    dc_saving_throw: int
    success_divide_damage_per_half: bool = False

    def run(self, attacker: Character, defender: List[Character]):
        if len(defender) > 1:
            raise error('Nao pode haver mais de um alvo nessa ação')

        if self.with_profiency_bonus:
            roll = attacker.roll_with_proficiency_bonus(
                self.atb,
                advantage=self.with_advantage,
                disadvantage=self.with_disadvantage,
            )
        elif self.with_profiency:
            roll = attacker.roll_with_proficiency(
                self.atb,
                prof=self.with_profiency,
                advantage=self.with_advantage,
                disadvantage=self.with_disadvantage,
            )
        else:
            roll = attacker.roll(
                self.atb,
                advantage=self.with_advantage,
                disadvantage=self.with_disadvantage,
            )

        roll += self.bonus_roll
        hit = defender[0].heath.is_ac_less_than(roll)
        
        if hit:
            damage = self.damage_roll.roll() + self.bonus_damage

            if self.sum_with_atb :
                damage += attacker.atbs.get_atb(self.sum_with_atb).value

            # Saving Throw
            roll_defender = defender[0].atbs.roll(self.atb_saving_throw)

            if roll_defender >= self.dc_saving_throw:
                if self.success_divide_damage_per_half:
                    damage = damage // 2
                else:
                    damage = 0
            # ------------

            defender[0].heath.take_damage(damage, self.damage_type)
            self.result = ((roll,defender[0].heath.ac),damage)
            self.success = True
        else:
            self.result = ((roll,defender[0].heath.ac))
            self.success = False
