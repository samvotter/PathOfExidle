import dataclasses


@dataclasses.dataclass(order=True)
class Item:
    level: int