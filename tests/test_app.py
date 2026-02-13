"""Tests for Flask routes."""

import json

from api.index import app


class TestRoutes:
    """Test cases for Flask routes."""

    @classmethod
    def setup_class(cls):
        """Set up test client."""
        cls.client = app.test_client()
        cls.app = app

    def test_index_route_returns_html(self):
        """Test that index route returns HTML."""
        response = self.client.get("/")

        assert response.status_code == 200
        assert b"html" in response.data.lower() or b"<!doctype" in response.data.lower()

    def test_generate_route_post_returns_image(self):
        """Test that generate route returns PNG image."""
        test_data = {
            "genre": "Test Genre",
            "product_name": "Test Product",
            "maker_name": "Test Maker",
            "reference_price": "1,234",
            "price_with_tax": "¥1,500",
            "base_price": "¥1,363",
        }

        response = self.client.post(
            "/generate",
            data=json.dumps(test_data),
            content_type="application/json",
        )

        assert response.status_code == 200
        assert response.content_type == "image/png"

    def test_generate_route_with_empty_data(self):
        """Test generate route with empty data."""
        test_data = {
            "genre": "",
            "product_name": "",
            "maker_name": "",
            "reference_price": "",
            "price_with_tax": "",
            "base_price": "",
        }

        response = self.client.post(
            "/generate",
            data=json.dumps(test_data),
            content_type="application/json",
        )

        # Should still return a valid image (using defaults)
        assert response.status_code == 200
        assert response.content_type == "image/png"

    def test_generate_route_with_price_values(self):
        """Test generate route with various price formats."""
        test_data = {
            "genre": "ガンプラ",
            "product_name": "RX-78-2 ガンダム",
            "maker_name": "バンダイ",
            "reference_price": "5,500",
            "price_with_tax": "¥6,050",
            "base_price": "¥5,500",
        }

        response = self.client.post(
            "/generate",
            data=json.dumps(test_data),
            content_type="application/json",
        )

        assert response.status_code == 200
        assert response.content_type == "image/png"
        assert len(response.data) > 0  # PNG should have some data
