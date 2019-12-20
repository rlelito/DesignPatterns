from concrete_subject import ConcreteSubject
from concrete_observer_1 import ConcreteObserver1
from concrete_observer_2 import ConcreteObserver2

if __name__ == "__main__":
    s = ConcreteSubject()

    o1 = ConcreteObserver1()
    s.attach(o1)
    o2 = ConcreteObserver2()
    s.attach(o2)

    s.some_logic()
    s.some_logic()

    s.detach(o1)

    s.some_logic()
