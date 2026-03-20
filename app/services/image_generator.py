from PIL import Image, ImageDraw, ImageFont

from app.domain.product import Product
from app.services.layout import (
    BASE_PRICE_POSITION,
    GENRE_POSITION,
    MAKER_POSITION,
    PRICE_POSITION,
    PRODUCT_NAME_POSITION,
    REFERENCE_PRICE_POSITION,
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
            fill=(0, 0, 0),
        )

        draw.text(
            (PRODUCT_NAME_POSITION.x, PRODUCT_NAME_POSITION.y),
            product.product_name,
            font=self.font_tiny,   # font_small → font_tiny（12px → 16px）
            fill=(0, 0, 0),
        )

        draw.text(
            (MAKER_POSITION.x, MAKER_POSITION.y),
            product.maker_name,
            font=self.font_medium,
            fill=(0, 0, 0),
        )

        draw.text(
            (REFERENCE_PRICE_POSITION.x, REFERENCE_PRICE_POSITION.y),
            product.reference_price,
            font=self.font_tiny,
            fill=(0, 0, 0),
        )

        draw.text(
            (PRICE_POSITION.x, PRICE_POSITION.y),
            product.price_with_tax,
            font=self.font_price_large,
            fill=(0, 0, 0),
        )

        draw.text(
            (BASE_PRICE_POSITION.x, BASE_PRICE_POSITION.y),
            product.base_price,
            font=self.font_tiny,
            fill=(0, 0, 0),
        )

        return img