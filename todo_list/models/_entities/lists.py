from dataclasses import dataclass

@dataclass(frozen=True)
class Model:
    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name
