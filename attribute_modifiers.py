import dataclasses
import enum


@dataclasses.dataclass(order=True)
class AttributeModifier:
    """
    Attributes can be modified in 1 of three ways:
        1. Add or minus.
            An absolute value is added or subtracted from the base value
        2. Increase or Decrease
            The base value is multiplied by the SUM of all modifiers
        3. More or less
            The base value is multiplied by the PRODUCT of all modifiers
    """
    add: int = 0
    minus: int = 0

    increase: int = 0
    decrease: int = 0

    less: int = 0
    more: int = 0


class CharacterAttributes(enum.Enum):
    # CORE ATTRIBUTES
    STRENGTH = 0
    DEXTERITY = 1
    INTELLIGENCE = 2

    DAMAGE
    SPEED
    ACCURACY
    CHANCE_ON_HIT
    AOE

    MOVEMENT
    FIND

    LIFE
    MANA
    REGENERATION
    
    ARMOR
    SHIELD
    DODGE
    BLOCK
