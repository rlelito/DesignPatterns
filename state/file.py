from __future__ import annotations
from file_states import FileClosed


class File(object):
    _state: FileState = None

    def __init__(self, state: FileState = FileClosed()) -> None:
        self.change_state(state)

    def open(self) -> None:
        self._state.open()

    def close(self) -> None:
        self._state.close()

    def read(self) -> None:
        self._state.read()

    def write(self) -> None:
        self._state.write()

    def change_state(self, state) -> None:
        if self._state is not None:
            print(f"\t[Changing state to: {type(state).__name__}]")
        self._state = state
        self._state.context = self
