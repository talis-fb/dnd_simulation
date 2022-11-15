from definitions.enums import TypesDamage,Conditions
from typing import List, Set
from utils.dices import Dices
import math

class Heath:
  def __init__(self,
      ac:int,
      hp:int,
      hp_dice: Dices,
      # Optionals
      resistance: Set[TypesDamage] = set(),
      vulnerability:Set[TypesDamage] = set(),
      invisible: Set[TypesDamage] = set(),
      conditions: Set[Conditions] = set(),
      hp_temp: int = 0,
   ) -> None:
      self.ac = ac
      self.hp = hp
      self.hp_max = hp # O maximo é o hp passado no inicio
      self.hp_dice = hp_dice
      self.resistance = resistance
      self.vulnerability = vulnerability
      self.invisible = invisible
      self.conditions = conditions
      self.hp_temp = hp_temp

  def is_dead(self) -> bool:
    return self.hp <= 0
  def is_alive(self) -> bool:
    return self.hp > 0

  def is_ac_less_than(self, amount:int) -> bool:
      return amount >= self.ac

  def add_hp(self, amount:int):
      self.hp += amount
      if self.hp > self.hp_max:
          self.hp = self.hp_max

  # Pontos TEMPORARIOS
  def add_temp_hp(self, amount:int):
      self.hp_temp = max([ self.hp_temp, amount ])
  def take_down_temp_hp(self, amount:int) -> int:
      difference = self.hp_temp - amount

      # Se é negativo, entao o passado é maior que a quantidade
      # disponivel de vida temporaria, entao ela deve ser zerada e 
      # ser retornado quando restou de dano apos o descontado nela
      if difference < 0:
          self.hp_temp = 0
          return -difference

      self.hp_temp = difference
      return 0


  def take_damage(self, amount:int, damage_type:TypesDamage | None = None):
      if damage_type:
          if damage_type in self.invisible:
              return # DO NOTHING
          if damage_type in self.resistance:
              amount = math.ceil(amount / 2)
          if damage_type in self.vulnerability:
              amount = amount * 2

      # Retira dos pontos temporarios primeiro
      rest_hp = self.take_down_temp_hp(amount)
      # Se sobrar hp, desconta do hp mesmo
      self.hp -= rest_hp

  # def take_down_hp_with_weapon(self, amount: int, weapon: Object, damage_type:TypesDamage = None):
  #     pass
