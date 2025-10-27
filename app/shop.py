from dataclasses import dataclass

@dataclass
class Shop:
    name: str
    location: tuple
    products: dict[str, float]