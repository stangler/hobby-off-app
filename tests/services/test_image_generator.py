from PIL import Image, ImageFont

from app.domain.product import Product
from app.services.image_generator import ImageGenerator


def test_generate_image() -> None:
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
        product_name="TestProductName",
        maker_name="TestMakerName",
        reference_price="1000",
        price_with_tax="1100",
        base_price="900",
    )

    img = generator.generate(product, base_image)

    assert img.size == (800, 600)
