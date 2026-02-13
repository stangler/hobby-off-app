#!/usr/bin/env python3
"""Flask application for Hobby OFF image generator.

Works both locally and on Vercel.
"""

from io import BytesIO
from pathlib import Path

from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont


def _get_static_paths() -> tuple[str, str]:
    """Determine static and templates directories based on deployment environment."""
    base_dir = Path(__file__).resolve().parent
    parent_dir = base_dir.parent

    if (base_dir / "static").exists():
        static_dir = str(base_dir / "static")
        templates_dir = str(base_dir / "templates")
    elif (parent_dir / "static").exists():
        static_dir = str(parent_dir / "static")
        templates_dir = str(parent_dir / "templates")
    else:
        static_dir = "static"
        templates_dir = "templates"

    return static_dir, templates_dir


STATIC_DIR, TEMPLATES_DIR = _get_static_paths()

# Flaskのテンプレートフォルダを設定
app = Flask(__name__)
app.template_folder = TEMPLATES_DIR

# フォントと画像のパス
bold_font_path = str(Path(STATIC_DIR) / "NotoSansJP-Bold.ttf")
regular_font_path = str(Path(STATIC_DIR) / "NotoSansJP-Regular.ttf")
base_image_path = str(Path(STATIC_DIR) / "base.png")


def generate_image(
    genre: str,
    product_name: str,
    maker_name: str,
    reference_price: str,
    price_with_tax: str,
    base_price: str,
) -> Image.Image:
    """Generate image with given parameters.

    Args:
        genre: Product genre/category.
        product_name: Name of the product.
        maker_name: Manufacturer name.
        reference_price: Reference market price.
        price_with_tax: Price including tax.
        base_price: Base price before tax.

    Returns:
        Generated PIL Image.

    """
    img = Image.open(base_image_path)
    draw = ImageDraw.Draw(img)

    # フォントサイズの設定
    font_medium = ImageFont.truetype(regular_font_path, 18)  # ジャンルと品名用
    font_small = ImageFont.truetype(regular_font_path, 12)  # メーカー名用(さらに小さく)
    font_tiny = ImageFont.truetype(regular_font_path, 16)  # 参考新品市場価格用
    font_price_large = ImageFont.truetype(bold_font_path, 50)  # 価格用

    # テキストの色
    text_color = (0, 0, 0)

    # 各フィールドにテキストを配置
    # ジャンル
    draw.text((115, 88), genre, font=font_medium, fill=text_color)

    # 品名
    draw.text((300, 88), product_name, font=font_medium, fill=text_color)

    # メーカー名
    draw.text((145, 136), maker_name, font=font_small, fill=text_color)

    # 参考新品市場価格
    draw.text((365, 145), f"¥{reference_price}", font=font_tiny, fill=text_color)

    # 報込価格
    draw.text((135, 170), price_with_tax, font=font_price_large, fill=text_color)

    # 本体価格
    draw.text((140, 261), base_price, font=font_small, fill=text_color)

    return img


@app.route("/")
def index() -> str:
    """Render the top page."""
    return render_template("form.html")


@app.route("/generate", methods=["POST"])
def generate() -> tuple[dict, int] | tuple[bytes, int]:
    """Generate and return image as response.

    Returns:
        Image file as bytes with 200 status, or error JSON with 500 status.

    """
    data = request.get_json()

    img = generate_image(
        genre=data.get("genre", ""),
        product_name=data.get("product_name", ""),
        maker_name=data.get("maker_name", ""),
        reference_price=data.get("reference_price", ""),
        price_with_tax=data.get("price_with_tax", ""),
        base_price=data.get("base_price", ""),
    )

    img_io = BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")


if __name__ == "__main__":
    # ローカル開発時の起動
    app.run(host="127.0.0.1", port=5000)
