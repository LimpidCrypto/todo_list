from enum import Enum
from typing import Dict
from serde import serde, from_dict
from todo_list.models._entities import BaseEntity

@serde
class Model():
    id: str
    name: str

    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name

class Entity(BaseEntity[Model]):
    def _deserialize(self, data: Dict[str, str]) -> Model:
        return from_dict(Model, data)

class Column(Enum):
    ID = "id"
    NAME = "name"
