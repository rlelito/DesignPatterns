from __future__ import annotations
from abc import ABC
from abc import abstractmethod


class FileState(ABC):
    _context: File = None

    @property
    def context(self) -> File:
        return self._context

    @context.setter
    def context(self, value: File) -> None:
        self._context = value

    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def read(self) -> None:
        pass

    @abstractmethod
    def write(self) -> None:
        pass


class FileOpened(FileState):
    def open(self) -> None:
        print("The file is already open.")

    def close(self) -> None:
        print("Closing the file.")
        self.context.change_state(FileClosed())

    def read(self):
        print("Reading from the file.")

    def write(self) -> None:
        print("Writing to the file.")


class FileClosed(FileState):
    def open(self) -> None:
        print("Opening the file.")
        self.context.change_state(FileOpened())

    def close(self) -> None:
        print("The file is already closed.")

    def read(self) -> None:
        print("The file closed - can't read from the file.")

    def write(self) -> None:
        print("The file closed - can't write to the file.")
