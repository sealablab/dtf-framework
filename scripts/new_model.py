#!/usr/bin/env python3
"""
Script to create new model files from template.
Usage: python new_model.py module_name "purpose" [--warning "warning text"] [--description "description"]
"""

import argparse
import os
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent.parent / "dtf_framework" / "models" / "_template.py"
MODELS_DIR = Path(__file__).parent.parent / "dtf_framework" / "models"

def create_model_file(module_name: str, purpose: str, warning: str = "", description: str = "", usage: str = ""):
    with open(TEMPLATE_PATH) as f:
        template = f.read()
    
    # Default warning if none provided
    if warning:
        warning_section = f"""## Warning
{warning}"""
    else:
        warning_section = ""
    
    # Default usage if none provided
    if usage:
        usage_section = f"""## Usage

```python
{usage}
```"""
    else:
        usage_section = ""
    
    content = template.format(
        module_name=module_name,
        purpose=purpose,
        warning_section=warning_section,
        description=description,
        usage_section=usage_section,
        imports="",  # Add default imports if needed
        code=""      # Add default code if needed
    )
    
    output_path = MODELS_DIR / f"{module_name}.py"
    with open(output_path, "w") as f:
        f.write(content)
    
    print(f"Created {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new model file from template")
    parser.add_argument("module_name", help="Name of the module (without .py)")
    parser.add_argument("purpose", help="Purpose of the module")
    parser.add_argument("--warning", help="Warning text (optional)")
    parser.add_argument("--description", help="Module description (optional)")
    parser.add_argument("--usage", help="Usage example (optional)")
    
    args = parser.parse_args()
    create_model_file(args.module_name, args.purpose, args.warning, args.description, args.usage) 