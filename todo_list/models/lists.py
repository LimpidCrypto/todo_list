from todo_list.core.data_manager import DataManager, DataList
from typing import List, Dict
from json import JSONDecodeError

def find_all_lists() -> List[Dict[str, str]]:
    try:
        return DataManager.read_all_entries(DataList.LISTS)
    except (FileNotFoundError, JSONDecodeError) as error:
        raise error
