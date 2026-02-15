# Hobby OFF Image Generator Application

## ファイル構成

```
hobby-off-app/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── domain/
│   │   ├── __init__.py
│   │   └── product.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── image.py
│   └── services/
│       ├── __init__.py
│       ├── image_generator.py
│       └── layout.py
├── static/
│   ├── base.png
│   ├── hobby_off_filled.png
│   ├── NotoSansJP-Bold.ttf
│   └── NotoSansJP-Regular.ttf
├── templates/
│   └── form.html
├── tests/
│   └── services/
│       ├── __init__.py
│       └── test_image_generator.py
├── e2e/
│   ├── form-submission.spec.ts
│   ├── utils.ts
│   └── validation.spec.ts
├── pyproject.toml
├── vercel.json
├── playwright.config.ts
├── package.json
├── pnpm-lock.yaml
├── run.py
└── README.md
```

## 開発環境のセットアップ

### 1. 依存関係のインストール

```bash
# Python 依存関係のインストール
uv sync

# Node.js 依存関係のインストール（E2Eテスト用）
pnpm install
```

### 2. アプリケーションの実行

```bash
# 開発サーバーの起動
uv run python run.py
```

## 使用方法

1. ブラウザでアプリケーションにアクセス
2. フォームに商品情報を入力
3. 「画像生成」ボタンをクリック
4. 生成された画像がプレビュー表示される
5. 「画像ダウンロード」ボタンで画像を保存

## コード品質とテストツール

### 静的解析ツール

#### Ruff（Pythonリンター）

```bash
# コードスタイルのチェック
uv run ruff check .

# 自動修正
uv run ruff check . --fix

# 特定のファイルのチェック
uv run ruff check app/services/image_generator.py
```

#### Pyright（Python型チェッカー）

```bash
# 型チェックの実行
uv run pyright

# 特定のファイルのチェック
uv run pyright app/services/image_generator.py
```

### テスト

#### 単体テスト（pytest）

```bash
# すべてのテストを実行
uv run pytest

# カバレッジ付きで実行
uv run pytest --cov=app

# 特定のテストファイルを実行
uv run pytest tests/services/test_image_generator.py

# 詳細表示で実行
uv run pytest -v
```

#### E2Eテスト（Playwright）

```bash
# テストの実行
pnpm exec playwright test
```
