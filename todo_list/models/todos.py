from serde import serde
from typing import Optional
from todo_list.models._entities import TodoModel, TodoEntity
from todo_list.core.data_store_manager import DataStoreManager, DataList
from json import JSONDecodeError
from serde import SerdeError
from uuid import uuid4, UUID

@serde
class NewTodoModel:
    name: str
    description: Optional[str] = None

    def __init__(self, name: str, description: Optional[str]) -> None:
        self.name = name
        self.description = description

def create_todo(list_uuid: UUID, todo: NewTodoModel) -> TodoModel:
    try:
        return TodoEntity().create(DataStoreManager, DataList.TODOS, TodoModel(id=str(uuid4()), name=todo.name, list_id=str(list_uuid), description=todo.description))
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error
