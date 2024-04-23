from todo_list.core.data_store_manager import DataStoreManager, DataList
from typing import List, Optional, Self, TypeVar, Generic, Dict
from json import JSONDecodeError
from serde import SerdeError, to_dict
from uuid import UUID
from abc import ABC, abstractmethod

M = TypeVar("M")

class BaseEntity(Generic[M], ABC):
    data_list: DataList
    entry_id: Optional[UUID] = None

    def create(self, dm: DataStoreManager, data_list: DataList, model: M) -> M:
        """Creates an entry in the data store.

        Args:
            dm (DataManager): The data manager to use.
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

    def one(self, dm: DataStoreManager) -> Optional[M]:
        """Finds one entry in the data store.

        Args:
            dm (DataManager): The data manager to use.

        Raises:
            FileNotFoundError: If the data store file is not found.
            JSONDecodeError: If the data store file is not a valid JSON file.
            SerdeError: If the data cannot be deserialized.

        Returns:
            Optional[M]: The deserialized model or None if not found.
        """
        try:
            all_entries = self._read_all(dm)
            if self.entry_id:
                for entry in all_entries:
                    match_entry = str(entry.id) == str(self.entry_id)
                    if match_entry:
                        return entry
                return None
            else:
                try:
                    return all_entries[0]
                except IndexError:
                    return None
        except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
            raise error

    def all(self, dm: DataStoreManager) -> List[M]:
        """Finds all entries in the data store.

        Args:
            dm (DataManager): The data manager to use.

        Raises:
            FileNotFoundError: If the data store file is not found.
            JSONDecodeError: If the data store file is not a valid JSON file.
            SerdeError: If the data cannot be deserialized.

        Returns:
            List[M]: The list of deserialized models.
        """
        try:
            return self._read_all(dm)
        except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
            raise error

    def remove(self, dm: DataStoreManager) -> None:
        """Removes an entry from the data store.

        Args:
            dm (DataManager): The data manager to use.

        Raises:
            FileNotFoundError: If the data store file is not found.
            JSONDecodeError: If the data store file is not a valid JSON file.
            SerdeError: If the data cannot be deserialized.

        Returns:
            int: The number of entries removed.
        """
        try:
            dm.remove_entry(self.data_list, str(self.entry_id))
        except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
            raise error

    def _read_all(self, dm: DataStoreManager) -> List[M]:
        """Reads all entries from the data store file.

        Args:
            dm (DataManager): The data manager to use.

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
                try:
                    arr.append(self._deserialize(entry))
                except SerdeError as error:
                    raise error
            return arr
        except (FileNotFoundError, JSONDecodeError) as error:
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
