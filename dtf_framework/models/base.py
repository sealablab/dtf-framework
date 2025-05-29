"""
# DTF Framework Models: base (dtf_framework.models.base)
## File Location
- Package: dtf_framework.models
- File: base.py
- Purpose: Base model definitions and common configurations

## Warning
This module is intended for internal use within the DTF framework.
You should **not** need to import __or__ inherit from this module directly.

This module defines the base model class and common configurations used throughout the DTF framework.
All model classes should inherit from DTFBaseModel to ensure consistent behavior.

"""

from pydantic import BaseModel, ConfigDict

class DTFBaseModel(BaseModel):
    """Base model with common configuration for all DTF models.
    
    This class provides a consistent foundation for all models in the DTF framework,
    ensuring uniform behavior and configuration across the codebase.
    """
    model_config = ConfigDict(
        extra="ignore",  # Ignore extra fields not defined in the model
        frozen=True,     # Make models immutable
        validate_assignment=True,  # Validate values on assignment
        str_strip_whitespace=True,  # Strip whitespace from strings
    )

class TestId(int):
    pass

class TestCmd(BaseModel):
    model_config = ConfigDict(extra="ignore")

class TestParams(BaseModel):
    model_config = ConfigDict(extra="ignore") 

class TestResults(BaseModel):
    model_config = ConfigDict(extra="ignore") 