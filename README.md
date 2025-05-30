# DTF Framework

> [!note] Cross-Platform Note
> This README is designed to render properly on GitHub, Bitbucket, and in Obsidian vaults.
> When viewing in Obsidian, you may want to use the "Reading View" for best results.

> [!important] Development Tools
> This is the core framework library. For development tools, scripts, and utilities,
> check out the [DTF Tools](https://github.com/sealablab/dtf-tools) repository.

## Overview

The DTF Framework is a Python package that provides core data models and utilities for the DTF system.
It is designed to be used as a dependency in other projects.

## Installation

```bash
# From PyPI
uv pip install dtf-framework

# From GitHub
uv pip install git+https://github.com/sealablab/dtf-framework.git
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
- [UV](https://github.com/astral-sh/uv) package manager

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
python scripts/new_model.py my_model "Purpose of my model" \
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
└── pyproject.toml        # Package configuration
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT

---

> [!tip] Obsidian Integration
> When using this in an Obsidian vault, you can:
> - Use the "Reading View" for best rendering
> - Create links to specific sections using the headers
> - Embed this README in other notes using `![[README]]` 