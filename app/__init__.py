from flask import Flask, render_template
from PIL import ImageFont

from app.config import Config
from app.routes.image import image_bp
from app.services.image_generator import ImageGenerator


def create_app() -> Flask:
    app = Flask(__name__, template_folder=str(Config.TEMPLATE_DIR))
    app.config.from_object(Config)

    static_dir = Config.STATIC_DIR

    font_medium = ImageFont.truetype(str(static_dir / "NotoSansJP-Regular.ttf"), 18)
    font_small = ImageFont.truetype(str(static_dir / "NotoSansJP-Regular.ttf"), 12)
    font_tiny = ImageFont.truetype(str(static_dir / "NotoSansJP-Regular.ttf"), 16)
    font_price_large = ImageFont.truetype(str(static_dir / "NotoSansJP-Bold.ttf"), 50)

    generator = ImageGenerator(
        font_medium,
        font_small,
        font_tiny,
        font_price_large,
    )

    app.config["image_generator"] = generator
    app.config["base_image_path"] = static_dir / "base.png"

    app.register_blueprint(image_bp)

    @app.route("/")
    def index() -> str:
        return render_template("form.html")

    return app
