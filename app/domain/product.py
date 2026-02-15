from dataclasses import dataclass
from typing import TypedDict


class ProductDict(TypedDict):
    genre: str
    title: str
    price: str


@dataclass(frozen=True)
class Product:
    genre: str
    title: str
    price: str

    @classmethod
    def from_dict(cls, data: ProductDict) -> "Product":
        return cls(
            genre=data["genre"],
            title=data["title"],
            price=data["price"],
        )
