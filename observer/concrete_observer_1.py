from observer import Observer
from subject import Subject


class ConcreteObserver1(Observer):
    def update(self, subject: Subject) -> None:
        if subject.subject_state < 4:
            print("\tConcreteObserver1: Reacted to the event")
