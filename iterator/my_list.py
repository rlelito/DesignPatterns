from typing import List


class MyList(object):
    def __init__(self, *args) -> None:
        self._list: List[int] = [*args]

    def count(self) -> int:
        return len(self._list)

    def append(self, element) -> None:
        self._list[self.count():] = [element]

    def remove(self, element) -> None:
        self._list.remove(element)

    def get(self, index) -> int:
        return self._list[index]

    def __str__(self):
        return f"List = {self._list}"
