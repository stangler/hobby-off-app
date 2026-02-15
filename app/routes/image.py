from io import BytesIO
from pathlib import Path
from typing import cast

from flask import Blueprint, Response, current_app, request, send_file
from PIL import Image

from app.domain.product import Product, ProductDict
from app.services.image_generator import ImageGenerator


image_bp = Blueprint("image", __name__)


@image_bp.route("/generate", methods=["POST"])
def generate() -> Response:
    data = request.get_json()

    if data is None:
        return Response("Invalid JSON", status=400)

    product = Product.from_dict(cast(ProductDict, data))

    generator = cast(ImageGenerator, current_app.config["image_generator"])
    base_image_path = cast(Path, current_app.config["base_image_path"])

    base_image = Image.open(base_image_path)

    img = generator.generate(product, base_image)

    img_io = BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")
