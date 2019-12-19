from list_iterator import ListIterator


class NonZeroListIterator(ListIterator):
    def current_item(self) -> int:
        if self.is_done():
            raise Exception("Iterator out of bounds")
        if self._list.get(self._current_index) == 0:
            self.next()
            self.current_item()
        return self._list.get(self._current_index)
