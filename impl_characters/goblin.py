from definitions.character import Character, CharacterSummary
from definitions.attributes import Atbs, Atb
from definitions.skills import SkillsName
from actions.impl.attacks.attacks import Attack_with_handaxe, Attack_with_bite
from utils.dices import Dices, d6

def create():
    return Character(
        CharacterSummary(
            name="Goblin",
            xp=50
        ),
        Atbs(
            strength=Atb(-1),
            dexterity=Atb(2),
            constitution=Atb(0),
            intelligence=Atb(0),
            wisdom=Atb(-1),
            charisma=Atb(-1),
            proficiency_bonus=2,
            ac=15,
            hp=7,
            hp_dice=Dices(2,d6)
        ),
        set([
            SkillsName.STEALTH
        ]),
        [
            Attack_with_bite(),
            Attack_with_handaxe()
        ]
    )
