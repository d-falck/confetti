<h1 align="center">🎊 Confetti 🎊</h1>

<p align="center">
  <a href="https://badge.fury.io/py/python-confetti"><img src="https://badge.fury.io/py/python-confetti.svg" alt="PyPI version"></a>
  <a href="https://pypi.org/project/python-confetti/"><img src="https://img.shields.io/pypi/pyversions/python-confetti.svg" alt="Python Versions"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
</p>

<p align="center">
  <b>Configure your Python scripts with magic ✨</b>
</p>

**Confetti** is a lightweight configuration management library for Python built on Pydantic. It lets you configure runs of your scripts using YAML files, with overrides from CLI arguments or environment variables. All you need is a Pydantic model and it'll handle the rest.

_This is a super simple wrapper for pydantic-settings right now but I plan to make it more feature-rich over time!_

## Installation

```bash
pip install python-confetti
```

## Quick Start

Create a configuration class that inherits from `BaseConfig`:

```python
from confetti import BaseConfig
from pydantic import Field

class Config(BaseConfig):
    name: str = Field(default="World", description="Name to greet")
    age: int = Field(default=25, description="Age of the person")
    verbose: bool = Field(default=False, description="Enable verbose output")

def main(config: Config):
    print(f"Hello, {config.name}!")
    if config.verbose:
        print(f"You are {config.age} years old.")

if __name__ == "__main__":
    main(Config())
```

Run your script with different configuration sources:

```bash
# Using defaults
python script.py

# Using CLI arguments
python script.py --name Alice --age 30 --verbose

# Using environment variables
export NAME=Bob
export AGE=35
python script.py

# Using a YAML config file
python script.py --config config.yaml
```

## Usage

### Configuration Sources (priority order)

1. **CLI arguments** - `python script.py --name Alice --age 30`
2. **Environment variables** - `export NAME=Bob`
3. **YAML config file** - `python script.py --config config.yaml`
4. **Defaults** - Values defined in your Config class

## Contributing

Contributions are welcome! Please feel free to submit a PR.

## License

MIT License
