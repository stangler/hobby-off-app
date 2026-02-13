"""Tests for image generation."""

from pathlib import Path

from PIL import Image

from api.index import generate_image


class TestGenerateImage:
    """Test cases for generate_image function."""

    def test_generate_image_returns_pil_image(self):
        """Test that generate_image returns a PIL Image."""
        img = generate_image(
            genre="Test Genre",
            product_name="Test Product",
            maker_name="Test Maker",
            reference_price="1,234",
            price_with_tax="¥1,500",
            base_price="¥1,363",
        )

        assert isinstance(img, Image.Image)

    def test_generate_image_with_empty_values(self):
        """Test generate_image with empty string values."""
        img = generate_image(
            genre="",
            product_name="",
            maker_name="",
            reference_price="",
            price_with_tax="",
            base_price="",
        )

        assert isinstance(img, Image.Image)

    def test_generate_image_with_long_values(self):
        """Test generate_image with long text values."""
        img = generate_image(
            genre="長いジャンル名",
            product_name="非常に長い商品名テスト",
            maker_name="製造者名テスト",
            reference_price="99,999",
            price_with_tax="¥999,999",
            base_price="¥909,090",
        )

        assert isinstance(img, Image.Image)

    def test_generate_image_has_correct_dimensions(self):
        """Test that generated image has expected dimensions."""
        img = generate_image(
            genre="Test",
            product_name="Product",
            maker_name="Maker",
            reference_price="100",
            price_with_tax="¥150",
            base_price="¥136",
        )

        # base.png should be the template
        base_path = Path(__file__).parent.parent / "static" / "base.png"
        if base_path.exists():
            base_img = Image.open(base_path)
            assert img.size == base_img.size
