import dataclasses
import enum


class DamageTypes(enum.Enum):
    PHYSICAL = 0
    FIRE = 1
    COLD = 2
    LIGHTNING = 3
    CHAOS = 4


@dataclasses.dataclass(frozen=True, order=True)
class Damage:
    amount: int
    type: DamageTypes




