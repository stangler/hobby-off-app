#!/usr/bin/env python3
"""
Flask application for Hobby OFF image generator
Works both locally and on Vercel
"""

from flask import Flask, render_template, request, send_file, jsonify
from PIL import Image, ImageDraw, ImageFont
import os
import io

app = Flask(__name__)

# パスの設定（ローカルとVercel両対応）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)

# staticとtemplatesのパスを探索
if os.path.exists(os.path.join(BASE_DIR, "static")):
    # api/static が存在する場合
    STATIC_DIR = os.path.join(BASE_DIR, "static")
    TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
elif os.path.exists(os.path.join(PARENT_DIR, "static")):
    # ../static が存在する場合（Vercelまたはapi/から実行）
    STATIC_DIR = os.path.join(PARENT_DIR, "static")
    TEMPLATES_DIR = os.path.join(PARENT_DIR, "templates")
else:
    # デフォルト
    STATIC_DIR = "static"
    TEMPLATES_DIR = "templates"

# Flaskのテンプレートフォルダを設定
app.template_folder = TEMPLATES_DIR

# フォントと画像のパス
bold_font_path = os.path.join(STATIC_DIR, "NotoSansJP-Bold.ttf")
regular_font_path = os.path.join(STATIC_DIR, "NotoSansJP-Regular.ttf")
base_image_path = os.path.join(STATIC_DIR, "base.png")

def generate_image(genre, product_name, maker_name, reference_price, price_with_tax, base_price):
    """画像を生成する関数"""
    # 画像を読み込む
    img = Image.open(base_image_path)
    draw = ImageDraw.Draw(img)
    
    # フォントサイズの設定
    font_medium = ImageFont.truetype(regular_font_path, 18)  # ジャンルと品名用
    font_small = ImageFont.truetype(regular_font_path, 12)  # メーカー名用（さらに小さく）
    font_tiny = ImageFont.truetype(regular_font_path, 16)  # 参考新品市場価格用
    font_price_large = ImageFont.truetype(bold_font_path, 50)  # 価格用
    
    # テキストの色
    text_color = (0, 0, 0)
    
    # 各フィールドにテキストを配置
    # ジャンル
    draw.text((115, 88), genre, font=font_medium, fill=text_color)
    
    # 品名
    draw.text((300, 88), product_name, font=font_medium, fill=text_color)
    
    # メーカー名（下に移動）
    draw.text((145, 136), maker_name, font=font_small, fill=text_color)
    
    # 参考新品市場価格
    draw.text((365, 145), f"¥{reference_price}", font=font_tiny, fill=text_color)
    
    # 報込価格
    draw.text((135, 170), price_with_tax, font=font_price_large, fill=text_color)
    
    # 本体価格（下に移動）
    draw.text((140, 261), base_price, font=font_small, fill=text_color)
    
    return img

@app.route('/')
def index():
    """トップページを表示"""
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate():
    """画像を生成してレスポンスとして返す"""
    try:
        # JSONデータを取得
        data = request.get_json()
        
        # 画像を生成
        img = generate_image(
            genre=data.get('genre', ''),
            product_name=data.get('product_name', ''),
            maker_name=data.get('maker_name', ''),
            reference_price=data.get('reference_price', ''),
            price_with_tax=data.get('price_with_tax', ''),
            base_price=data.get('base_price', '')
        )
        
        # 画像をバイトストリームに保存
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png')
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Vercel用のハンドラ
handler = app

if __name__ == '__main__':
    # ローカル開発時の起動
    app.run(debug=True, host='0.0.0.0', port=5000)

