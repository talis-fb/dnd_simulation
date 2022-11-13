# from definitions.actions import Actions
from definitions.character import Character, CharacterSummary
from definitions.attributes import Atbs, Atb
from definitions.skills import SkillsName
from impl_actions.attacks import Attack_with_dagger

goblin = Character(
    CharacterSummary(
        name="Goblin",
        level=1
    ),
    Atbs(
        strength=Atb(2),
        dexterity=Atb(2),
        constitution=Atb(2),
        intelligence=Atb(2),
        wisdom=Atb(2),
        charisma=Atb(2),
    ),
    set([ SkillsName.ANIMAL_HANDLING ]),
    [
        Attack_with_dagger(),
    ]
)

goblin2 = Character(
    CharacterSummary(
        name="Goblin",
        level=1
    ),
    Atbs(
        strength=Atb(2),
        dexterity=Atb(2),
        constitution=Atb(2),
        intelligence=Atb(2),
        wisdom=Atb(2),
        charisma=Atb(2),
    ),
    set([ SkillsName.ANIMAL_HANDLING ]),
    [
        Attack_with_dagger(),
    ]
)
