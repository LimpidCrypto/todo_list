from serde import serde
from typing import Optional, List
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


def create_todo(
    list_uuid: UUID, todo: NewTodoModel, todo_uuid: Optional[UUID] = None
) -> TodoModel:
    try:
        uuid = uuid4()
        if todo_uuid:
            uuid = todo_uuid
        return TodoEntity().create(
            DataStoreManager,
            DataList.TODOS,
            TodoModel(
                id=str(uuid),
                name=todo.name,
                list_id=str(list_uuid),
                description=todo.description,
            ),
        )
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error


def find_todo_by_id(todo_uuid: UUID) -> Optional[TodoModel]:
    try:
        return TodoEntity().find_by_id(DataList.TODOS, todo_uuid).one(DataStoreManager)
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error


def find_todo_list_items(list_uuid: UUID) -> List[TodoModel]:
    try:
        return (
            TodoEntity()
            .find(DataList.TODOS)
            .where("list_id", str(list_uuid))
            .all(DataStoreManager)
        )
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error


def edit_todo_list_item(list_uuid: UUID, item_uuid: UUID, todo: NewTodoModel):
    try:
        remove_todo_list_item(list_uuid, item_uuid)
        return create_todo(list_uuid, todo, item_uuid)
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error


def remove_todo_list_item(list_uuid: UUID, item_uuid: UUID):
    try:
        TodoEntity().find(DataList.TODOS).where("id", str(item_uuid)).where(
            "list_id", str(list_uuid)
        ).remove(DataStoreManager)
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error
