from flask import request, Blueprint
from werkzeug.exceptions import InternalServerError, BadRequest
from todo_list.models import find_all_lists, remove_list_by_id, create_list, NewListModel
from todo_list.controllers.validations import validate_list_existence
from serde import to_dict, SerdeError
from serde.json import from_json
from typing import Tuple, Union, Dict, List
from json import JSONDecodeError
from uuid import UUID

LIST_BLUEPRINT = Blueprint('list', __name__)

@LIST_BLUEPRINT.errorhandler(InternalServerError)
@LIST_BLUEPRINT.errorhandler(BadRequest)
def post_new_list() -> Tuple[Union[str, Dict[str, str]], int]:
    """The controller for creating a new todo list.

    Returns:
        Tuple[Union[str, Dict[str, str]], int]: A tuple containing the new todo list or an error message and status code.
    """
    try:
        list_model = str(request.json).replace("'", '"')
        new_entry = create_list(from_json(NewListModel, list_model))
        return to_dict(new_entry), 201
    except BadRequest:
        return 'Invalid request', 400
    except (FileNotFoundError, JSONDecodeError, SerdeError):
        return 'Unable to create new todo list', 500

@LIST_BLUEPRINT.errorhandler(InternalServerError)
def get_all_lists() -> Tuple[List[Dict[str, str]], int]:
    """The controller for getting all todo lists.

    Returns:
        Tuple[List[Dict[str, str]], int]: A tuple containing a list of todo lists or an error message and status code.
    """
    try:
        list_models = find_all_lists()
        list_model_list = []
        for list_model in list_models:
            list_model_list.append(to_dict(list_model))
        return list_model_list, 200
    except (FileNotFoundError, JSONDecodeError, SerdeError):
        return 'Unable to get lists', 500

@LIST_BLUEPRINT.errorhandler(InternalServerError)
@LIST_BLUEPRINT.errorhandler(BadRequest)
def delete_list_by_id(list_id: str) -> Tuple[str, int]:
    """The controller for deleting a todo list by its ID.

    Args:
        list_id (str): The UUID of the todo list to delete.

    Returns:
        Tuple[str, int]: A tuple containing an error message and status code if the todo list does not exist, otherwise an empty string and status code.
    """
    try:
        list_uuid = UUID(list_id)
        is_error = validate_list_existence(list_uuid)
        if is_error:
            return is_error
        remove_list_by_id(list_uuid)
        return '', 204
    except ValueError:
        return 'Invalid list uuid', 400
    except (FileNotFoundError, JSONDecodeError, SerdeError):
        return 'Unable to delete todo list', 500


LIST_BLUEPRINT.add_url_rule('/list/<list_id>', view_func=delete_list_by_id, methods=['DELETE'])
LIST_BLUEPRINT.add_url_rule('/list', view_func=post_new_list, methods=['POST'])
LIST_BLUEPRINT.add_url_rule('/lists', view_func=get_all_lists, methods=['GET'])
