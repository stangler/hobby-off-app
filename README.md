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

## Code Quality and Testing Tools

### Ruff (Python Linter)

```bash
# Install ruff
uv add ruff

# Run ruff to check code style
uv run ruff check .

# Automatically fix issues
uv run ruff check . --fix

# Check specific file or directory
uv run ruff check api/
```

### Pyright (Python Type Checker)

```bash
# Install pyright
uv add pyright

# Run pyright to check type annotations
uv run pyright

# Check specific file
uv run pyright api/index.py
```

### Pytest (Python Testing Framework)

```bash
# Install pytest
uv add pytest

# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=api

# Run specific test file
uv run pytest tests/test_app.py

# Run tests in verbose mode
uv run pytest -v
```
