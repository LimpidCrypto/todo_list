from flask import request, Blueprint
from werkzeug.exceptions import InternalServerError, NotFound, BadRequest
from todo_list.models import find_all_lists, find_list_by_id, remove_list_by_id, create_list, NewListModel
from serde import to_dict, SerdeError
from serde.json import from_json
from json import JSONDecodeError
from uuid import UUID

LIST_BLUEPRINT = Blueprint('list', __name__)

@LIST_BLUEPRINT.errorhandler(InternalServerError)
@LIST_BLUEPRINT.errorhandler(BadRequest)
@LIST_BLUEPRINT.errorhandler(NotFound)
def get_list_by_id(list_id):
    try:
        list_uuid = UUID(list_id)
    except ValueError:
        return 'Invalid list uuid', 400
    try:
        list_model = find_list_by_id(list_uuid)
        if not list_model:
            return 'Todo list not found', 404
        return to_dict(list_model), 200
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        return 'Unable to get todo list', 500

@LIST_BLUEPRINT.errorhandler(InternalServerError)
@LIST_BLUEPRINT.errorhandler(BadRequest)
def delete_list_by_id(list_id):
    try:
        list_uuid = UUID(list_id)
    except ValueError:
        return 'Invalid list uuid', 400
    try:
        remove_list_by_id(list_uuid)
        return '', 204
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        return 'Unable to delete todo list', 500


def post_new_list():
    try:
        list_model = str(request.json).replace("'", '"')
        new_entry = create_list(from_json(NewListModel, list_model))
        return to_dict(new_entry), 201
    except BadRequest:
        return 'Invalid request', 400


# define endpoint for getting all lists
@LIST_BLUEPRINT.errorhandler(InternalServerError)
def get_all_lists():
    try:
        list_models = find_all_lists()
        list_model_list = []
        for list_model in list_models:
            list_model_list.append(to_dict(list_model))
        return list_model_list, 200
    except Exception:
        return 'Unable to get all todo lists', 500


LIST_BLUEPRINT.add_url_rule('/list/<list_id>', view_func=get_list_by_id, methods=['GET'])
LIST_BLUEPRINT.add_url_rule('/list/<list_id>', view_func=delete_list_by_id, methods=['DELETE'])
LIST_BLUEPRINT.add_url_rule('/list', view_func=post_new_list, methods=['POST'])
LIST_BLUEPRINT.add_url_rule('/lists', view_func=get_all_lists, methods=['GET'])
