from flask import request, Blueprint
from werkzeug.exceptions import InternalServerError, NotFound, BadRequest
from todo_list.models import (
    create_todo,
    NewTodoModel,
    find_todo_list_items,
    edit_todo_list_item,
    remove_todo_list_item,
)
from todo_list.controllers.validations import (
    validate_list_existence,
    validate_todo_existence,
)
from serde import to_dict, SerdeError
from serde.json import from_json
from json import JSONDecodeError
from uuid import UUID

TODO_BLUEPRINT = Blueprint("todo", __name__)


@TODO_BLUEPRINT.errorhandler(InternalServerError)
@TODO_BLUEPRINT.errorhandler(BadRequest)
@TODO_BLUEPRINT.errorhandler(NotFound)
def post_new_todo(list_id: str):
    try:
        list_uuid = UUID(list_id)
        is_error = validate_list_existence(list_uuid)
        if is_error:
            return is_error
        todo_model = str(request.json).replace("'", '"')
        new_entry = create_todo(list_uuid, from_json(NewTodoModel, todo_model))
        return to_dict(new_entry), 201
    except ValueError:
        return "Invalid request", 400
    except (FileNotFoundError, JSONDecodeError, SerdeError):
        return "Unable to create todo", 500


@TODO_BLUEPRINT.errorhandler(InternalServerError)
@TODO_BLUEPRINT.errorhandler(BadRequest)
@TODO_BLUEPRINT.errorhandler(NotFound)
def get_todo_list_items(list_id: str):
    try:
        list_uuid = UUID(list_id)
        is_error = validate_list_existence(list_uuid)
        if is_error:
            return is_error
        items = find_todo_list_items(list_uuid)
        return to_dict(items), 200
    except ValueError:
        return "Invalid UUID", 400
    except (FileNotFoundError, JSONDecodeError, SerdeError):
        return "Unable to get todo list items", 500


@TODO_BLUEPRINT.errorhandler(InternalServerError)
@TODO_BLUEPRINT.errorhandler(BadRequest)
@TODO_BLUEPRINT.errorhandler(NotFound)
def patch_todo_list_item(list_id: str, item_id: str):
    try:
        list_uuid = UUID(list_id)
        list_item_uuid = UUID(item_id)
        is_error = validate_todo_existence(list_item_uuid)
        if is_error:
            return is_error
        todo_model = str(request.json).replace("'", '"')
        new_item = edit_todo_list_item(
            list_uuid, list_item_uuid, from_json(NewTodoModel, todo_model)
        )
        return to_dict(new_item), 200
    except ValueError:
        return "Invalid UUID", 400
    except (FileNotFoundError, JSONDecodeError, SerdeError):
        return "Unable to edit todo list item", 500


def delete_todo_list_item(list_id: str, item_id: str):
    try:
        list_uuid = UUID(list_id)
        list_item_uuid = UUID(item_id)
        is_error = validate_todo_existence(list_item_uuid)
        if is_error:
            return is_error
        remove_todo_list_item(list_uuid, list_item_uuid)
        return "", 204
    except ValueError:
        return "Invalid UUID", 400
    except (FileNotFoundError, JSONDecodeError, SerdeError):
        return "Unable to delete todo list item", 500


TODO_BLUEPRINT.add_url_rule(
    "/list/<list_id>", view_func=get_todo_list_items, methods=["GET"]
)
TODO_BLUEPRINT.add_url_rule(
    "/list/<list_id>/item", view_func=post_new_todo, methods=["POST"]
)
TODO_BLUEPRINT.add_url_rule(
    "/list/<list_id>/item/<item_id>", view_func=patch_todo_list_item, methods=["PATCH"]
)
TODO_BLUEPRINT.add_url_rule(
    "/list/<list_id>/item/<item_id>",
    view_func=delete_todo_list_item,
    methods=["DELETE"],
)
