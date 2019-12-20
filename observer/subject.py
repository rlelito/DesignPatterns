from abc import ABC
from abc import abstractmethod
from observer import Observer


class Subject(ABC):
    _subject_state: int = None

    @abstractmethod
    def attach(self, o: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, o: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

    @property
    def subject_state(self) -> int:
        return self._subject_state
