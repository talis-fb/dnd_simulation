from src.core.character import Character, CharacterSummary
from src.core.attributes import Atbs, Atb
from src.core.combat_stats import Heath
from src.core.dices import Dices, d8
from src.impl.itens.weapons.melee import Lanca
from src.impl.itens.weapons.ranged import ArcoLongo
from src.impl.actions.attacks.bites import Attack_Bite

def create():

    actions = [
        Lanca(),
        ArcoLongo(),
        Attack_Bite()
    ]

    return Character(
        CharacterSummary(
            name="Gnoll",
            xp=100
        ),
        Atbs(
            strength=Atb(2),
            dexterity=Atb(1),
            constitution=Atb(0),
            intelligence=Atb(-2),
            wisdom=Atb(0),
            charisma=Atb(-2),
            proficiency_bonus=2,
        ),
        Heath(
            ac=15,
            hp=22,
            hp_dice=Dices(5,d8)
        ),
        set([]),
        actions,
    )
