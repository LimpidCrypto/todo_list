from todo_list.core.data_store_manager import DataStoreManager, DataList
from typing import List, Optional, Self, TypeVar, Generic, Dict, Any
from json import JSONDecodeError
from serde import SerdeError, to_dict
from uuid import UUID
from abc import ABC, abstractmethod

M = TypeVar("M")


class BaseEntity(Generic[M], ABC):
    matching_entries: List[M] = []
    data_list: DataList
    where_list: List[Dict[str, Any]] = []
    entry_id: Optional[UUID] = None

    def __init__(self):
        self.matching_entries = []
        self.where_list = []
        self.entry_id = None

    def find(self, data_list: DataList) -> Self:
        """Finds entries in the data store.

        Args:
            data_list (DataList): The data list to use.

        Returns:
            Self: The entity instance.
        """
        self.data_list = data_list
        return self

    def find_by_id(self, data_list: DataList, entry_id: UUID) -> Self:
        """Finds an entry in the data store by its ID.

        Args:
            data_list (DataList): The data list to use.
            entry_id (str): The ID of the entry to find.

        Returns:
            Self: The entity instance.
        """
        self.data_list = data_list
        self.entry_id = entry_id
        return self

    def where(self, field: str, value: Any) -> Self:
        """Filters entries in the data store by a field value.

        Args:
            field (str): The field to filter by.
            value (Any): The value to filter by.

        Returns:
            Self: The entity instance.
        """
        self.where_list.append({field: value})
        return self

    def create(self, dm: DataStoreManager[M], data_list: DataList, model: M) -> M:
        """Creates an entry in the data store.

        Args:
            dm (DataStoreManager): The data manager to use.
            model (M): The model to create.

        Raises:
            FileNotFoundError: If the data store file is not found.
            JSONDecodeError: If the data store file is not a valid JSON file.
            SerdeError: If the data cannot be serialized.

        Returns:
            M: The created model.
        """
        try:
            dm.write_entry(data_list, to_dict(model))
            return model
        except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
            raise error

    def one(self, dm: DataStoreManager[M]) -> Optional[M]:
        """Finds one entry in the data store.

        Args:
            dm (DataStoreManager): The data manager to use.

        Raises:
            FileNotFoundError: If the data store file is not found.
            JSONDecodeError: If the data store file is not a valid JSON file.
            SerdeError: If the data cannot be deserialized.

        Returns:
            Optional[M]: The deserialized model or None if not found.
        """
        try:
            self._read_all(dm)
            if self.matching_entries:
                return self.matching_entries[0]
            return None
        except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
            raise error

    def all(self, dm: DataStoreManager[M]) -> List[M]:
        """Finds all entries in the data store.

        Args:
            dm (DataStoreManager): The data manager to use.

        Raises:
            FileNotFoundError: If the data store file is not found.
            JSONDecodeError: If the data store file is not a valid JSON file.
            SerdeError: If the data cannot be deserialized.

        Returns:
            List[M]: The list of deserialized models.
        """
        try:
            self._read_all(dm)
            return self.matching_entries
        except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
            raise error

    def remove(self, dm: DataStoreManager[M]) -> None:
        """Removes an entry from the data store.

        Args:
            dm (DataStoreManager): The data manager to use.

        Raises:
            FileNotFoundError: If the data store file is not found.
            JSONDecodeError: If the data store file is not a valid JSON file.
            SerdeError: If the data cannot be deserialized.

        Returns:
            int: The number of entries removed.
        """
        try:
            self._read_all(dm)
            dm.remove_entry(self.data_list, self.matching_entries)
        except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
            raise error

    def _read_all(self, dm: DataStoreManager[M]):
        """Reads all entries from the data store file.

        Args:
            dm (DataStoreManager): The data manager to use.

        Raises:
            FileNotFoundError: If the data store file is not found.
            JSONDecodeError: If the data store file is not a valid JSON file.
            SerdeError: If the data cannot be deserialized.

        Returns:
            List[M]: The list of deserialized models.
        """
        try:
            arr = []
            for entry in dm.read_all_entries(self.data_list):
                is_match = True
                # check if all where conditions are met
                for where in self.where_list:
                    for key, value in where.items():
                        if entry[key] != value:
                            is_match = False
                # check if id is set and matches
                if self.entry_id:
                    is_match = entry["id"] == str(self.entry_id)
                if is_match:
                    arr.append(self._deserialize(entry))
            self.matching_entries = arr
        except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
            raise error

    @abstractmethod
    def _deserialize(self, data: Dict[str, str]) -> M:
        """An abstract method to deserialize data into the model.

        Args:
            data (Dict[str, str]): The data to deserialize.

        Raises:
            SerdeError: If the data cannot be deserialized.

        Returns:
            M: The deserialized model.
        """
        pass
