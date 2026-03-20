from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class TextPosition:
    x: int
    y: int


GENRE_POSITION: Final = TextPosition(115, 88)
PRODUCT_NAME_POSITION: Final = TextPosition(300, 88)
MAKER_POSITION: Final = TextPosition(160, 125)            # (125,132) → (160,125)
REFERENCE_PRICE_POSITION: Final = TextPosition(385, 143)  # ✅ このまま
PRICE_POSITION: Final = TextPosition(100, 172)            # ✅ このまま
BASE_PRICE_POSITION: Final = TextPosition(175, 256)       # ✅ このまま