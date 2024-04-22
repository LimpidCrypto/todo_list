from dataclasses import dataclass

@dataclass(frozen=True)
class Model:
    def __init__(self, id: str, name: str, description: str, list: str) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.list = list
