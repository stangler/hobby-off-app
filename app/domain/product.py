from dataclasses import dataclass
from typing import TypedDict


class ProductDict(TypedDict):
    genre: str
    product_name: str
    maker_name: str
    reference_price: str
    price_with_tax: str
    base_price: str


@dataclass(frozen=True)
class Product:
    genre: str
    product_name: str
    maker_name: str
    reference_price: str
    price_with_tax: str
    base_price: str

    @classmethod
    def from_dict(cls, data: ProductDict) -> "Product":
        return cls(
            genre=data["genre"],
            product_name=data["product_name"],
            maker_name=data["maker_name"],
            reference_price=data["reference_price"],
            price_with_tax=data["price_with_tax"],
            base_price=data["base_price"],
        )
