from json import JSONDecodeError
from typing import Optional, Tuple
from uuid import UUID
from todo_list.models import find_list_by_id, find_todo_by_id
from serde import SerdeError


def validate_list_existence(list_id: UUID) -> Optional[Tuple[str, int]]:
    """Validate the existence of a todo list.

    Args:
        list_id (UUID): The UUID of the todo list to validate.

    Returns:
        Optional[Tuple[str, int]]: A tuple containing an error message and
            status code if the todo list does not exist, otherwise None.
    """
    try:
        list_model = find_list_by_id(list_id)
        if not list_model:
            return "Todo list not found", 404
        return None
    except (FileNotFoundError, JSONDecodeError, SerdeError):
        return "Unable to check todo list existence", 500


def validate_todo_existence(todo_id: UUID) -> Optional[Tuple[str, int]]:
    """Validate the existence of a todo item.

    Args:
        todo_id (UUID): The UUID of the todo item to validate.

    Returns:
        Optional[Tuple[str, int]]: A tuple containing an error message and
            status code if the todo item does not exist, otherwise None.
    """
    try:
        todo_model = find_todo_by_id(todo_id)
        if not todo_model:
            return "Todo item not found", 404
        return None
    except (FileNotFoundError, JSONDecodeError, SerdeError):
        return "Unable to check todo item existence", 500
