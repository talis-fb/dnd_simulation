from enum import Enum

class TypesDamage(Enum):
  ACID = 'acid'
  BLUDGEONING = 'bludgeoning'
  COLD = 'cold'
  FIRE = 'fire'
  FORCE = 'force'
  LIGHTNING = 'lightning'
  NECROTIC = 'necrotic'
  PIERCING = 'piercing'
  POISON = 'poison'
  PSYCHIC = 'psychic'
  RADIANT = 'radiant'
  SLASHING = 'slashing'
  THUNDER = 'thunder'

class Conditions(Enum):
  BLINDED = 'blinded'
  CHARMED = 'charmed'
  DEAFENED = 'deafened'
  EXHAUSTION = 'exhaustion'
  FRIGHTENED = 'frightened'
  GRAPPLED = 'grappled'
  INCAPACITATED = 'incapacitated'
  INVISIBLE = 'invisible'
  PARALYZED = 'paralyzed'
  PETRIFIED = 'petrified'
  POISONED = 'poisoned'
  PRONE = 'prone'
  RESTRAINED = 'restrained'
  STUNNED = 'stunned'
  UNCONSCIOUS = 'unconscious'