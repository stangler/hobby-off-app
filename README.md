# Hobby OFF Image Generator Application

## Unified File Structure (Local & Vercel Compatible)

```
project_folder/
├── api/
│   └── index.py          # Main application
├── static/
│   ├── base.png
│   ├── NotoSansJP-Bold.ttf
│   └── NotoSansJP-Regular.ttf
├── templates/
│   └── form.html
├── vercel.json           # Vercel configuration
└── pyproject.toml        # uv dependency management
```

## Local Development Setup (using uv)

### 1. Install Dependencies

```bash
# If uv is not installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

### 2. Run the Application

```bash
# Run api/index.py directly
uv run python api/index.py
```

or

```bash
cd api
uv run python index.py
```


## Usage

1. Access the application in your browser
2. Enter product information in the form
3. Click "Generate Image" button
4. The generated image will be displayed in preview
5. Download the image using "Download Image" button
