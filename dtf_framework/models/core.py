"""
# DTF Framework Core Models (dtf_framework.models.core)

## File Location
- Package: dtf_framework.models
- File: core.py
- Purpose: Core model definitions

This module defines the core models used throughout the DTF framework.
These models represent the fundamental data structures and types used in the system.

## Usage

```python
from dtf_framework.models.core import TestId, TestCmd, TestParams
```


"""

from .base import DTFBaseModel
from .types import TestIdType

class TestId(TestIdType):
    """Test identifier type.
    
    This class represents a unique identifier for tests in the DTF framework.
    It inherits from int to provide integer-like behavior while allowing for
    future extension of test ID functionality.
    """
    pass

class TestCmd(DTFBaseModel):
    """Test command model.
    
    This model represents a command to be executed as part of a test.
    It inherits from DTFBaseModel to ensure consistent behavior with other models.
    """
    pass

class TestParams(DTFBaseModel):
    """Test parameters model.
    
    This model represents the parameters for a test execution.
    It inherits from DTFBaseModel to ensure consistent behavior with other models.
    """
    pass 