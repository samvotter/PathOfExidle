import dataclasses
import abc

from items.item import Item


@dataclasses.dataclass(order=True)
class Equipment(Item, abc.ABC):
    required_level: int
    required_strength: int
    required_dexterity: int
    required_intelligence: int

    @abc.abstractmethod
    def equip(self):
        """
        What happens when the character equips this?
        """

    @abc.abstractmethod
    def unequip(self):
        """
        What happens when the character unequips this?
        """