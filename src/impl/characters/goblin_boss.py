from src.core.character import Character, CharacterSummary
from src.core.attributes import Atbs, Atb
from src.core.skills import SkillsName
from src.core.combat_stats import Heath
from src.core.dices import Dices, d6
from src.impl.itens.weapons.melee import CimitarraWithDexterity, Azagaia
from src.impl.actions.multiple_attacks import Multiple_attacks

def summary():
    return CharacterSummary(
        name="Chefe Goblin",
        xp=200
    )

def create():

    # MOVES SPECIFICATIONS
    Cimitarra = CimitarraWithDexterity()
    Cimitarra.with_profiency_bonus = True

    return Character(
        summary(),
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
            ac=17,
            hp=21,
            hp_dice=Dices(6,d6)
        ),
        set([
            SkillsName.STEALTH
        ]),
        # Actions
        [
            Multiple_attacks([
                Cimitarra,
                Cimitarra,
            ]),
            Multiple_attacks([
                Cimitarra,
                Cimitarra,
            ]),
            Multiple_attacks([
                Cimitarra,
                Cimitarra,
            ]),
            Multiple_attacks([
                Cimitarra,
                Cimitarra,
            ]),
            Azagaia()
        ],

        #Itens
        # [ 
        #     CimitarraWithDexterity(),
        # ]
    )
