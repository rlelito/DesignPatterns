from __future__ import annotations
from abc import abstractmethod


class HelpHandler(object):
    _next_handler: HelpHandler = None

    @abstractmethod
    def handle_help(self) -> None:
        if self._next_handler:
            return self._next_handler.handle_help()
        return None

    @classmethod
    def show_help(cls) -> None:
        pass

    def has_help(self) -> bool:
        return "show_help" in self.__class__.__dict__

    @property
    def next_handler(self) -> HelpHandler:
        return self._next_handler

    @next_handler.setter
    def next_handler(self, value) -> None:
        self._next_handler = value
