from attribute_modifiers import Attribute

import dataclasses
import enum


@dataclasses.dataclass(order=True)
class Character:
    level: Attribute =          Attribute(base=1)
    strength: Attribute =       Attribute()
    dexterity: Attribute =      Attribute()
    intelligence: Attribute =   Attribute()


class DefaultClasses(enum.Enum):
    MARAUDER = Character(
        level=Attribute(base=1),
        strength=Attribute(base=32),
        dexterity=Attribute(base=14),
        intelligence=Attribute(base=14)
    )
    RANGER = Character(
        level=Attribute(base=1),
        strength=Attribute(base=14),
        dexterity=Attribute(base=32),
        intelligence=Attribute(base=14)
    )
    WITCH = Character(
        level=Attribute(base=1),
        strength=Attribute(base=32),
        dexterity=Attribute(base=14),
        intelligence=Attribute(base=14)
    )
    DUELIST = Character(
        level=Attribute(base=1),
        strength=Attribute(base=23),
        dexterity=Attribute(base=23),
        intelligence=Attribute(base=14)
    )
    TEMPLAR = Character(
        level=Attribute(base=1),
        strength=Attribute(base=23),
        dexterity=Attribute(base=14),
        intelligence=Attribute(base=23)
    )
    SHADOW = Character(
        level=Attribute(base=1),
        strength=Attribute(base=14),
        dexterity=Attribute(base=23),
        intelligence=Attribute(base=23)
    )
    ASCENDANT = Character(
        level=Attribute(base=1),
        strength=Attribute(base=20),
        dexterity=Attribute(base=20),
        intelligence=Attribute(base=20)
    )