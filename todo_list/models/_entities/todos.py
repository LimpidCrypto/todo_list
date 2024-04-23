from enum import Enum
from typing import Optional, Dict
from serde import serde, from_dict
from todo_list.models._entities import BaseEntity

@serde
class Model:
    id: str
    name: str
    list_id: str
    description: Optional[str] = None

    def __init__(self, id: str, name: str, list_id: str, description: Optional[str]) -> None:
        self.id = id
        self.name = name
        self.list_id = list_id
        self.description = description

class Entity(BaseEntity[Model]):
    def _deserialize(self, data: Dict[str, str]) -> Model:
        return from_dict(Model, data)

class Column(Enum):
    ID = "id"
    NAME = "name"
    DESCRIPTION = "description"
    LIST_ID = "list_id"
