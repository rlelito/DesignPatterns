from typing import List
from random import randrange
from subject import Subject
from observer import Observer


class ConcreteSubject(Subject):
    _subject_state: int = None
    _observers: List[Observer] = []

    def attach(self, o: Observer) -> None:
        print("Subject.attach()")
        self._observers.append(o)

    def detach(self, o: Observer) -> None:
        self._observers.remove(o)

    def notify(self) -> None:
        print("Subject.notify()")
        for o in self._observers:
            o.update(self)

    def some_logic(self) -> None:
        print("\nSubject.some_logic()")
        self._subject_state = randrange(0, 10)
        print(f"\tSubject._subject_state = {self._subject_state}")
        self.notify()
