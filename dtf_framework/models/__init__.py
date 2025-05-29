"""
# DTF Framework (dtf_framework.models.base)
## File Location
- Package: dtf_framework.models
- File: __init__.py
- Purpose: Package initialization and model exports

This package provides the core data models used throughout the DTF framework.
It is organized into several modules:

- base.py: Base model definitions and common configurations
- types.py: Type aliases and constants
- core.py: Core model definitions

## Usage

```python
# Import specific models
from dtf_framework.models import TestId, TestCmd, TestParams
```
"""

from .base import DTFBaseModel
from .core import TestId, TestCmd, TestParams
from .types import TestIdType

__all__ = [
    # Base models
    'DTFBaseModel',
    
    # Core models
    'TestId',
    'TestCmd',
    'TestParams',
    
    # Types
    'TestIdType',
] 