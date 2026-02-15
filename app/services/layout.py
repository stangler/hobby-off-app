from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class TextPosition:
    x: int
    y: int


GENRE_POSITION: Final = TextPosition(115, 88)
TITLE_POSITION: Final = TextPosition(115, 120)
PRICE_POSITION: Final = TextPosition(480, 320)
