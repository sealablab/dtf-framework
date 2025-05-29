#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    print("Sourcing venv env")
    # Get the absolute path to the virtual environment
    venv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".venv")
    
    # Activate virtual environment by modifying PATH
    venv_bin = os.path.join(venv_path, "bin")
    os.environ["PATH"] = f"{venv_bin}:{os.environ['PATH']}"
    
    print("Installing dev packages")
    # Run uv pip install with the -e flag
    try:
        subprocess.run(["uv", "pip", "install", "-e", ".[dev]"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: 'uv' command not found. Please make sure uv is installed.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 