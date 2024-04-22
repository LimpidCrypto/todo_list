from todo_list.models._entities.lists import Model as ListModel
from todo_list.models._entities.lists import Column as ListColumn
from todo_list.models._entities.todos import Model as TodoModel
from todo_list.models._entities.todos import Column as TodoColumn

from todo_list.core.data_manager import DataManager, DataList
from typing import List, Optional, Self, TypeVar
from enum import Enum
from json import JSONDecodeError
from uuid import UUID

M = TypeVar("M")
C = TypeVar("C")

class Entity:
    DATA_LIST: DataList
    entry_id: Optional[str]

    def __init__(self, entry_id: Optional[str]) -> None:
        if entry_id:
            try:
                UUID(entry_id, version=4)
                self.entry_id = entry_id
            except ValueError:
                raise ValueError("Invalid UUID")

    def find() -> Self:
        try:
            return Entity()
        except Exception as error:
            raise error

    def find_by_id(entry_id: str) -> Self:
        try:
            return Entity(entry_id)
        except Exception as error:
            raise error

    def find_by_column(column: C) -> Self:
        try:
            return Entity()
        except Exception as error:
            raise error

    def one(self, dm: DataManager) -> M:
        try:
            all_entries = self._read_all(dm)
            if self.entry_id:
                for entry in all_entries:
                    if entry["id"] == self.entry_id:
                        return entry
                return {}
            else:
                try:
                    return all_entries[0]
                except IndexError:
                    return {}
        except (FileNotFoundError, JSONDecodeError) as error:
            raise error

    def all(self, dm: DataManager) -> List[M]:
        try:
            return self._read_all(dm)
        except (FileNotFoundError, JSONDecodeError) as error:
            raise error

    def _read_all(self, dm: DataManager) -> List[M]:
        try:
            return dm.read_all_entries(self.DATA_LIST)
        except (FileNotFoundError, JSONDecodeError) as error:
            raise error


__all__ = [
    "ListModel",
    "ListColumn",
    "TodoModel",
    "TodoColumn"
]
