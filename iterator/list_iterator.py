from my_list import MyList


class ListIterator(object):
    def __init__(self, obj_list: MyList) -> None:
        self._current_index: int = 0
        self._list: MyList = obj_list

    def first(self) -> None:
        self._current_index = 0

    def next(self) -> None:
        self._current_index += 1

    def is_done(self) -> bool:
        return self._current_index >= self._list.count()

    def current_item(self) -> int:
        if self.is_done():
            raise Exception("Iterator out of bounds")
        return self._list.get(self._current_index)
