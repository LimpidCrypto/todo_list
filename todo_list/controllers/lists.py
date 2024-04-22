from todo_list.core.data_manager import DataManager, DataList
from flask import request, jsonify, abort, Blueprint
from werkzeug.exceptions import InternalServerError
from todo_list.models import find_all_lists

LIST_BLUEPRINT = Blueprint('list', __name__)

# define endpoint for getting and deleting existing todo lists
def handle_list(list_id):
    # find todo list depending on given list id
    list_item = None
    for l in todo_lists:
        if l['id'] == list_id:
            list_item = l
            break
    # if the given list id is invalid, return status code 404
    if not list_item:
        abort(404)
    if request.method == 'GET':
        # find all todo entries for the todo list with the given id
        print('Returning todo list...')
        return jsonify([i for i in todos if i['list'] == list_id])
    elif request.method == 'DELETE':
        # delete list with given id
        print('Deleting todo list...')
        todo_lists.remove(list_item)
        return '', 200


# define endpoint for adding a new list
def add_new_list():
    # make JSON from POST data (even if content type is not set correctly)
    new_list = request.get_json(force=True)
    print('Got new list to be added: {}'.format(new_list))
    # create id for new list, save it and return the list with id
    new_list['id'] = uuid.uuid4()
    todo_lists.append(new_list)
    return jsonify(new_list), 200


# define endpoint for getting all lists
@LIST_BLUEPRINT.errorhandler(InternalServerError)
def get_all_lists():
    try:
        return jsonify(find_all_lists()), 200
    except Exception:
        return 'Unable to get all todo lists', 500


LIST_BLUEPRINT.add_url_rule('/list/<list_id>', view_func=handle_list, methods=['GET', 'DELETE'])
LIST_BLUEPRINT.add_url_rule('/list', view_func=add_new_list, methods=['POST'])
LIST_BLUEPRINT.add_url_rule('/lists', view_func=get_all_lists, methods=['GET'])
