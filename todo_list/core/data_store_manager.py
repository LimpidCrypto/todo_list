from todo_list.constants import ROOT_DIR
from pathlib import Path
import json
from typing import List, Dict, Generic, TypeVar
from enum import Enum
from abc import ABC


class DataList(Enum):
    LISTS = "lists"
    TODOS = "todos"


M = TypeVar("M")


class DataStoreManager(Generic[M], ABC):
    DATA_PATH = ROOT_DIR.joinpath("data")

    def _build_data_list_path(data_list: DataList) -> Path:
        return DataStoreManager.DATA_PATH.joinpath(f"{data_list.value}.json")

    def _read_data(data_list: DataList) -> List[Dict[str, str]]:
        try:
            with open(DataStoreManager._build_data_list_path(data_list), "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as error:
            raise error

    def _write_data(data_list: DataList, data: List[Dict[str, str]]) -> None:
        try:
            with open(DataStoreManager._build_data_list_path(data_list), "w") as file:
                json.dump(data, file)
        except (FileNotFoundError, TypeError) as error:
            raise error

    def write_entry(data_list: DataList, entry: Dict[str, str]) -> None:
        try:
            data = DataStoreManager._read_data(data_list)
        except (FileNotFoundError, json.JSONDecodeError) as error:
            raise error
        data.append(entry)
        try:
            return DataStoreManager._write_data(data_list, data)
        except (FileNotFoundError, TypeError) as error:
            raise error

    def read_entry(data_list: DataList, entry_id: str) -> Dict[str, str]:
        try:
            data = DataStoreManager._read_data(data_list)
        except (FileNotFoundError, json.JSONDecodeError) as error:
            raise error
        for entry in data:
            if entry["id"] == entry_id:
                return entry
        return {}

    def remove_entry(data_list: DataList, entries: List[M]) -> None:
        try:
            data = DataStoreManager._read_data(data_list)
        except (FileNotFoundError, json.JSONDecodeError) as error:
            raise error
        new_data = []
        for entry in data:
            if entry["id"] not in [entry.id for entry in entries]:
                new_data.append(entry)
        try:
            return DataStoreManager._write_data(data_list, new_data)
        except (FileNotFoundError, TypeError) as error:
            raise error

    def read_all_entries(data_list: DataList) -> List[Dict[str, str]]:
        try:
            return DataStoreManager._read_data(data_list)
        except (FileNotFoundError, json.JSONDecodeError) as error:
            raise error
