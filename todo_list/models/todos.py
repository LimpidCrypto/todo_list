from serde import serde
from typing import Optional, List
from todo_list.models._entities import TodoModel, TodoEntity, TodoColumn
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
    """Creates a new todo list item in the data store.

    Args:
        list_uuid (UUID): The ID of the todo list.
        todo (NewTodoModel): The new todo list item to create.
        todo_uuid (Optional[UUID], optional): The todo list items ID if a specific one needs to be used. Defaults to None.

    Raises:
        FileNotFoundError: If the data store file is not found.
        JSONDecodeError: If the data store file is not a valid JSON file.
        SerdeError: If the data cannot be serialized.

    Returns:
        TodoModel: The created todo list item.
    """
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
    """Finds a todo list item by its ID in the data store.

    Args:
        todo_uuid (UUID): The ID of the todo list item.

    Raises:
        FileNotFoundError: If the data store file is not found.
        JSONDecodeError: If the data store file is not a valid JSON file.
        SerdeError: If the data cannot be deserialized.

    Returns:
        Optional[TodoModel]: The todo list item if found, otherwise None.
    """
    try:
        return TodoEntity().find_by_id(DataList.TODOS, todo_uuid).one(DataStoreManager)
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error


def find_todo_list_items(list_uuid: UUID) -> List[TodoModel]:
    """Finds all todo list items of a given list id in the data store.

    Args:
        list_uuid (UUID): The ID of the todo list.

    Raises:
        FileNotFoundError: If the data store file is not found.
        JSONDecodeError: If the data store file is not a valid JSON file.
        SerdeError: If the data cannot be deserialized.

    Returns:
        List[TodoModel]: The list of todo list items.
    """
    try:
        return (
            TodoEntity()
            .find(DataList.TODOS)
            .where(TodoColumn.LIST_ID, str(list_uuid))
            .all(DataStoreManager)
        )
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error


def edit_todo_list_item(list_uuid: UUID, item_uuid: UUID, todo: NewTodoModel) -> TodoModel:
    """Edits a todo list item in the data store.

    Args:
        list_uuid (UUID): The ID of the todo list.
        item_uuid (UUID): The ID of the todo list item.
        todo (NewTodoModel): The new todo list item to replace the old one.

    Raises:
        FileNotFoundError: If the data store file is not found.
        JSONDecodeError: If the data store file is not a valid JSON file.
        SerdeError: If the data cannot be serialized.

    Returns:
        TodoModel: The edited todo list item.
    """
    try:
        remove_todo_list_item(list_uuid, item_uuid)
        return create_todo(list_uuid, todo, item_uuid)
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error


def remove_todo_list_item(list_uuid: UUID, item_uuid: UUID):
    """Removes a todo list item from the data store.

    Args:
        list_uuid (UUID): The ID of the todo list.
        item_uuid (UUID): The ID of the todo list item.

    Raises:
        FileNotFoundError: If the data store file is not found.
        JSONDecodeError: If the data store file is not a valid JSON file.
        SerdeError: If the data cannot be serialized.
    """
    try:
        TodoEntity().find(DataList.TODOS).where(TodoColumn.ID, str(item_uuid)).where(
            TodoColumn.LIST_ID, str(list_uuid)
        ).remove(DataStoreManager)
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error
