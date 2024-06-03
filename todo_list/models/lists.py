from todo_list.core.data_store_manager import DataStoreManager, DataList
from typing import List, Optional
from json import JSONDecodeError
from todo_list.models._entities import ListEntity, ListModel
from serde import SerdeError, serde
from uuid import UUID, uuid4


@serde
class NewListModel:
    name: str

    def __init__(self, name: str):
        self.name = name


def create_list(list_model: NewListModel) -> ListModel:
    """Creates a new todo list in the data store.

    Args:
        list_model (NewListModel): The new todo list to create.

    Raises:
        FileNotFoundError: If the data store file is not found.
        JSONDecodeError: If the data store file is not a valid JSON file.
        SerdeError: If the data cannot be serialized.

    Returns:
        ListModel: The created todo list.
    """
    try:
        return ListEntity().create(
            DataStoreManager,
            DataList.LISTS,
            ListModel(id=str(uuid4()), name=list_model.name),
        )
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error


def find_all_lists() -> List[ListModel]:
    """Finds all todo lists in the data store.

    Raises:
        FileNotFoundError: If the data store file is not found.
        JSONDecodeError: If the data store file is not a valid JSON file.
        SerdeError: If the data cannot be deserialized.

    Returns:
        List[ListModel]: The list of todo lists.
    """
    try:
        return ListEntity().find(DataList.LISTS).all(DataStoreManager)
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error


def find_list_by_id(list_id: UUID) -> Optional[ListModel]:
    """Finds a todo list in the data store by its ID.

    Args:
        list_id (UUID): The ID of the todo list to find.

    Raises:
        FileNotFoundError: If the data store file is not found.
        JSONDecodeError: If the data store file is not a valid JSON file.
        SerdeError: If the data cannot be deserialized.

    Returns:
        Optional[ListModel]: The todo list if found, otherwise None.
    """
    try:
        return ListEntity().find_by_id(DataList.LISTS, list_id).one(DataStoreManager)
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error


def remove_list_by_id(list_id: UUID) -> None:
    """Removes a todo list from the data store by its ID.

    Args:
        list_id (UUID): The ID of the todo list to remove.

    Raises:
        FileNotFoundError: If the data store file is not found.
        JSONDecodeError: If the data store file is not a valid JSON file.
        SerdeError: If the data cannot be deserialized.
    """
    try:
        return ListEntity().find_by_id(DataList.LISTS, list_id).remove(DataStoreManager)
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error
