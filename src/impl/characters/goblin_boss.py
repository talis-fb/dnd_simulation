from src.core.character import Character, CharacterSummary
from src.core.attributes import Atbs, Atb
from src.core.skills import SkillsName
from src.core.combat_stats import Heath
from src.core.dices import Dices, d6
from src.impl.itens.weapons.melee import CimitarraWithDexterity
from src.impl.itens.weapons.ranged import ArcoCurto

def create():
    return Character(
        CharacterSummary(
            name="Chefe Goblin",
            xp=200
        ),
        Atbs(
            strength=Atb(0),
            dexterity=Atb(2),
            constitution=Atb(0),
            intelligence=Atb(0),
            wisdom=Atb(-1),
            charisma=Atb(0),
            proficiency_bonus=2,
        ),
        Heath(
            ac=15,
            hp=7,
            hp_dice=Dices(2,d6)
        ),
        set([
            SkillsName.STEALTH
        ]),
        # Actions
        [
            CimitarraWithDexterity(),
            ArcoCurto()
        ],

        #Itens
        # [ 
        #     CimitarraWithDexterity(),
        # ]
    )
