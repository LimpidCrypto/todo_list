from dataclasses import dataclass
from enum import Enum
import serde
from . import Entity
from todo_list.core.data_manager import DataList

class Column(Enum):
    ID = "id"
    NAME = "name"

@serde
@dataclass(frozen=True)
class Model(Entity):
    DATA_LIST = DataList.LISTS
    ENTITY_COLUMNS = Column

    id: str
    name: str

    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name
        self.ENTITY_COLUMNS.NAME
