from src.core.character import Character, CharacterSummary
from src.core.attributes import Atbs, Atb
from src.core.skills import SkillsName
from src.core.combat_stats import Heath
from src.impl.actions.attacks.attacks import Attack_with_bite, Attack_with_handaxe
from src.core.dices import Dices, d6

def create():
    return Character(
        CharacterSummary(
            name="Goblin",
            xp=50
        ),
        Atbs(
            strength=Atb(1),
            dexterity=Atb(2),
            constitution=Atb(0),
            intelligence=Atb(0),
            wisdom=Atb(-1),
            charisma=Atb(-1),
            proficiency_bonus=2,
        ),
        Heath(
            ac=15,
            hp=17,
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
