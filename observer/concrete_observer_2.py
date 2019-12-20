from observer import Observer
from subject import Subject


class ConcreteObserver2(Observer):
    def update(self, subject: Subject) -> None:
        if subject.subject_state == 0 or subject.subject_state >= 3:
            print("\tConcreteObserver2: Reacted to the event")
