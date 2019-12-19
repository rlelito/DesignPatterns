from __future__ import annotations
from typing import Optional


class Singleton(object):
    _instance: Optional[Singleton] = None

    def __init__(self) -> None:
        if Singleton._instance is not None:
            raise Exception("Class is a Singleton")
        else:
            Singleton._instance = self

    @staticmethod
    def get_instance() -> None:
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

    @staticmethod
    def message_1() -> None:
        print("Message 1")

    @staticmethod
    def message_2() -> None:
        print("Message 2")
