import dataclasses
import enum
import typing

from items.equipment.equipment import Equipment


@dataclasses.dataclass(order=True)
class Weapon(Equipment):
    damage_floor: int
    damage_ceiling: int
    attack_speed: int
    range: int
    critical: int
    modifiers: ... # typing.List[AttributeModifiers]


@dataclasses.dataclass(order=True)
class OneHandedWeapon(Weapon):

    def equip(self):
        """
        OneHandedWeapon can occupy either the main-hand slot or the off-hand slot
        """
        pass

    def unequip(self):
        """
        OneHandedWeapons do not lockout off-hand slots
        """


@dataclasses.dataclass(order=True)
class TwoHandedWeapon(Weapon):

    def equip(self):
        """
        TwoHandedWeapon must occupy the main-hand slot and locks out the off-hand slot
        """

    def unequip(self):
        """
        TwoHandWeapons should release the lockout on offhand slots.
        """

