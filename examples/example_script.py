from confetti import BaseConfig
from pydantic import Field


class Config(BaseConfig):
    name: str = Field(default="John Doe", description="Your name")
    age: int = Field(default=25, description="Your age")


def main(config: Config):
    print(f"Hello, {config.name}!")
    print(f"You are {config.age} years old.")


if __name__ == "__main__":
    main(Config())
