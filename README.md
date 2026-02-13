# Hobby OFF 画像生成アプリケーション

## 統一されたファイル構成（ローカル・Vercel共通）

```
プロジェクトフォルダ/
├── api/
│   └── index.py          # メインアプリケーション
├── static/
│   ├── base.png
│   ├── NotoSansJP-Bold.ttf
│   └── NotoSansJP-Regular.ttf
├── templates/
│   └── form.html
├── vercel.json           # Vercel設定
├── pyproject.toml        # uv依存関係管理
└── requirements.txt      # Vercel用（uvから生成）
```

## ローカル開発環境でのセットアップ（uv使用）

### 1. 依存関係のインストール

```bash
# uvがインストールされていない場合
curl -LsSf https://astral.sh/uv/install.sh | sh

# 依存関係をインストール
uv sync
```

### 2. アプリケーションの起動

```bash
# api/index.pyを直接実行
uv run python api/index.py
```

または

```bash
cd api
uv run python index.py
```

### 3. ブラウザでアクセス

```
http://localhost:5000
```

## Vercelへのデプロイ

### 1. requirements.txtの生成

Vercelはuvをサポートしていないため、requirements.txtを生成します：

```bash
uv pip compile pyproject.toml -o requirements.txt
```

### 2. デプロイ手順

1. GitHubにリポジトリを作成
2. すべてのファイルをコミット・プッシュ
   ```bash
   git add .
   git commit -m "Initial commit"
   git push
   ```
3. Vercelダッシュボードで「New Project」をクリック
4. GitHubリポジトリを選択
5. 「Deploy」をクリック

### 3. 注意事項

- `static/` フォルダに必ず以下のファイルを配置：
  - `base.png`
  - `NotoSansJP-Bold.ttf`
  - `NotoSansJP-Regular.ttf`
- `templates/` フォルダに `form.html` を配置
- Vercelデプロイ前に `requirements.txt` を生成してコミット

## 使い方

1. ブラウザでアプリケーションにアクセス
2. フォームに商品情報を入力
3. 「画像を生成」ボタンをクリック
4. 生成された画像がプレビュー表示される
5. 「画像をダウンロード」ボタンでダウンロード可能

## トラブルシューティング

### Vercelでエラーが出る場合

1. ファイル構成を確認（上記の構成と一致しているか）
2. `static/` と `templates/` フォルダが正しく配置されているか確認
3. フォントファイルと画像ファイルがコミットされているか確認
4. `requirements.txt` が最新か確認
   ```bash
   uv pip compile pyproject.toml -o requirements.txt
   ```

### ローカルでポート5000が使用中の場合

`api/index.py` の最終行を変更：

```python
app.run(debug=True, host='0.0.0.0', port=8000)  # ポート番号を変更
```

### パスエラーが出る場合

`api/index.py` は自動的にパスを探索するため、以下のどちらの方法でも起動可能：

```bash
# ルートディレクトリから実行
python api/index.py

# apiディレクトリから実行
cd api && python index.py
```

## uvコマンド早見表

```bash
# 依存関係の追加
uv add パッケージ名

# 依存関係の削除
uv remove パッケージ名

# 依存関係の同期
uv sync

# アプリケーションの実行
uv run python api/index.py

# requirements.txtの生成（Vercel用）
uv pip compile pyproject.toml -o requirements.txt
```

## ファイル構成の利点

- **統一性**: ローカルとVercelで同じファイル構成
- **シンプル**: `api/index.py` がメインファイル
- **自動パス解決**: どこから実行しても動作する

