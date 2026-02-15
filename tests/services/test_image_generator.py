from pathlib import Path

from PIL import Image, ImageFont

from app.domain.product import Product
from app.services.image_generator import ImageGenerator


def test_generate_image(tmp_path: Path) -> None:
    font = ImageFont.load_default()

    generator = ImageGenerator(
        font,
        font,
        font,
        font,
    )

    base_image = Image.new("RGB", (800, 600), "white")

    product = Product(
        genre="TestGenre",
        title="TestTitle",
        price="1000",
    )

    img = generator.generate(product, base_image)

    assert img.size == (800, 600)
