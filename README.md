# DTF Framework

> [!note] Cross-Platform Note
> This README is designed to render properly on GitHub, Bitbucket, and in Obsidian vaults.
> When viewing in Obsidian, you may want to use the "Reading View" for best results.

## Overview

The DTF Framework is a Python package that provides core data models and utilities for the DTF system.
It is designed to be used as a dependency in other projects.

## Installation

```bash
# From PyPI
pip install dtf-framework

# From Artifactory
pip install dtf-framework --index-url https://your-artifactory-url/api/pypi/pypi/simple
```

## Quick Start

```python
from dtf_framework.models import TestId, TestCmd, TestParams

# Create a test command
cmd = TestCmd(...)
```

## Development

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Setup

```bash
# Clone the repository
git clone https://github.com/sealablab/dtf-framework.git
cd dtf-framework

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # or .venv/Scripts/activate on Windows

# Install development dependencies
uv pip install -e ".[dev]"
```

### Creating New Models

We provide a script to create new model files with proper templates:

```bash
./scripts/new_model.py my_model "Purpose of my model" \
    --warning "Optional warning" \
    --description "Optional description"
```

## Project Structure

```
dtf-framework/
├── dtf_framework/          # The actual Python package
│   ├── models/            # Core data models
│   │   ├── _template.py   # Model template
│   │   ├── __init__.py
│   │   ├── base.py       # Base model definitions
│   │   ├── core.py       # Core model implementations
│   │   └── types.py      # Type definitions
│   └── __init__.py
├── scripts/               # Development scripts
├── tests/                # Test directory
└── pyproject.toml        # Package configuration
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `pytest`
5. Submit a pull request

## License

[Your chosen license]

---

> [!tip] Obsidian Integration
> When using this in an Obsidian vault, you can:
> - Use the "Reading View" for best rendering
> - Create links to specific sections using the headers
> - Embed this README in other notes using `![[README]]` 