from dataclasses import dataclass
from enum import Enum
from typing import Optional

@dataclass(frozen=True)
class Model:
    id: str
    name: str
    list: str
    description: Optional[str] = None

    def __init__(self, id: str, name: str, list: str, description: Optional[str]) -> None:
        self.id = id
        self.name = name
        self.list = list
        self.description = description

class Column(Enum):
    ID = "id"
    NAME = "name"
    DESCRIPTION = "description"
    LIST = "list"
