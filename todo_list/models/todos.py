from dataclasses import dataclass

@dataclass(frozen=True)
class NewTodo:
    def __init__(self, name: str, description: str, list: str) -> None:
        self.name = name
        self.description = description
        self.list = list
