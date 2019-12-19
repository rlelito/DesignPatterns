from my_list import MyList
from list_iterator import ListIterator
from non_zero_list_iterator import NonZeroListIterator

if __name__ == "__main__":
    data = [1, 2, 0, 0, 5, 6, 1, 0, 9, 8, 3, 0]
    ml = MyList(*data)

    print("Iterator passing through whole list:")
    i = ListIterator(ml)
    i.first()
    while not i.is_done():
        print(i.current_item(), end=', ')
        i.next()

    print("\n\nIterator passing through only non zero elements of list:")
    nzi = NonZeroListIterator(ml)
    nzi.first()
    while not nzi.is_done():
        try:
            print(nzi.current_item(), end=', ')
            nzi.next()
        except:
            pass  # last elem is 0
