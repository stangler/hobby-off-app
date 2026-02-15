from PIL import Image, ImageDraw, ImageFont

from app.domain.product import Product
from app.services.layout import (
    GENRE_POSITION,
    PRICE_POSITION,
    TITLE_POSITION,
)

FontType = ImageFont.ImageFont | ImageFont.FreeTypeFont


class ImageGenerator:
    def __init__(
        self,
        font_medium: FontType,
        font_small: FontType,
        font_tiny: FontType,
        font_price_large: FontType,
    ) -> None:
        self.font_medium = font_medium
        self.font_small = font_small
        self.font_tiny = font_tiny
        self.font_price_large = font_price_large

    def generate(self, product: Product, base_image: Image.Image) -> Image.Image:
        img = base_image.copy()
        draw = ImageDraw.Draw(img)

        draw.text(
            (GENRE_POSITION.x, GENRE_POSITION.y),
            product.genre,
            font=self.font_medium,
        )

        draw.text(
            (TITLE_POSITION.x, TITLE_POSITION.y),
            product.product_name,
            font=self.font_small,
        )

        draw.text(
            (PRICE_POSITION.x, PRICE_POSITION.y),
            product.price_with_tax,
            font=self.font_price_large,
        )

        return img
