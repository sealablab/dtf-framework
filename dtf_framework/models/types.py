"""
# File: dtf_framework/models/types.py

# DTF Framework Types

This module defines core type aliases and constants used throughout the DTF framework.
It serves as a central location for type definitions to ensure consistency across the codebase.

## Warning
If you are referencing these datatypes outside of `dtf_framework.models.base`, you are probably doing something wrong.

## Usage

```python
from dtf_framework.models.types import TestIdType
```

## File Location
- Package: dtf_framework.models
- File: types.py
- Purpose: Type definitions and constants
"""

from typing import TypeAlias

# Core type definitions
TestIdType: TypeAlias = int 