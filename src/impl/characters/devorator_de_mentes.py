from src.core.character import Character, CharacterSummary
from src.core.attributes import Atbs, Atb
from src.core.enums.atbs import AtbsNames
from src.core.enums.types_damage import TypesDamage
from src.core.skills import SkillsName
from src.core.combat_stats import Heath
from src.core.dices import Dices, d8, d10
from src.impl.actions.attacks.abstracts import Attack_one_target, Attack_one_target_with_saving_throw

class Tentaculos(Attack_one_target):
    atb = AtbsNames.INTELLIGENCE
    with_profiency_bonus = True
    sum_with_atb = AtbsNames.INTELLIGENCE
    damage_roll = Dices(2, d10)
    damage_type = TypesDamage.PSYCHIC

class ExtrairCerebros(Attack_one_target):
    atb = AtbsNames.INTELLIGENCE
    with_profiency_bonus = True
    sum_with_atb = AtbsNames.INTELLIGENCE
    damage_roll = Dices(10, d10)
    damage_type = TypesDamage.PSYCHIC

class RajadaMental(Attack_one_target_with_saving_throw):
    atb_saving_throw = AtbsNames.INTELLIGENCE
    dc_saving_throw = 15
    atb = AtbsNames.INTELLIGENCE
    with_profiency_bonus = True
    sum_with_atb = AtbsNames.INTELLIGENCE
    damage_roll = Dices(10, d10)
    damage_type = TypesDamage.PSYCHIC


def create():
    actions = [
        Tentaculos(),
        RajadaMental(),
        ExtrairCerebros(),
    ]

    return Character(
        CharacterSummary(
            name="Devorador de Mentes",
            xp=2900
        ),
        Atbs(
            strength=Atb(0),
            dexterity=Atb(1),
            constitution=Atb(1),
            intelligence=Atb(4),
            wisdom=Atb(3),
            charisma=Atb(3),
            proficiency_bonus=3,
            saving_throws=set([ AtbsNames.INTELLIGENCE, AtbsNames.WISDOM, AtbsNames.CHARISMA ])
        ),
        Heath(
            ac=15,
            hp=71,
            hp_dice=Dices(13,d8)
        ),
        set([
            SkillsName.ARCANA,
            SkillsName.DECEPTION,
            SkillsName.INSIGHT,
            SkillsName.PERCEPTION,
            SkillsName.PERSUASION,
            SkillsName.STEALTH,
        ]),
        actions,
    )
