from flask import request, Blueprint
from werkzeug.exceptions import InternalServerError, NotFound, BadRequest
from todo_list.models import create_todo, NewTodoModel, find_list_by_id
from serde import to_dict, SerdeError
from serde.json import from_json
from json import JSONDecodeError
from uuid import UUID
from typing import Optional, Tuple

TODO_BLUEPRINT = Blueprint('todo', __name__)

@TODO_BLUEPRINT.errorhandler(InternalServerError)
@TODO_BLUEPRINT.errorhandler(BadRequest)
@TODO_BLUEPRINT.errorhandler(NotFound)
def post_new_todo(list_id):
    try:
        list_uuid = UUID(list_id)
        is_error = _validate_list_existence(list_uuid)
        if is_error:
            return is_error
        todo_model = str(request.json).replace("'", '"')
    except (ValueError):
        return 'Invalid request', 400
    try:
        new_entry = create_todo(list_uuid, from_json(NewTodoModel, todo_model))
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        print(error)
        return 'Unable to create todo', 500

    return to_dict(new_entry), 201

def get_todo_list(list_id):
    try:
        list_uuid = UUID(list_id)
        is_error = _validate_list_existence(list_uuid)
        if is_error:
            return is_error
        todo_model = str(request.json).replace("'", '"')
    except (ValueError):
        return 'Invalid request', 400
    try:
        new_entry = create_todo(list_uuid, from_json(NewTodoModel, todo_model))
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        print(error)
        return 'Unable to create todo', 500

    return to_dict(new_entry), 201

def _validate_list_existence(list_id: UUID) -> Optional[Tuple[str, int]]:
    try:
        list_model = find_list_by_id(list_id)
        if not list_model:
            return 'Todo list not found', 404
        return None
    except (FileNotFoundError, JSONDecodeError, SerdeError):
        return 'Unable to check todo list existence', 500

TODO_BLUEPRINT.add_url_rule('/list/<list_id>', view_func=get_todo_list, methods=['GET'])
TODO_BLUEPRINT.add_url_rule('/list/<list_id>/item', view_func=post_new_todo, methods=['POST'])
