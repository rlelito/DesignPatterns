from library_v1 import LibraryV1
from library_v2 import LibraryV2
from rectangle import Rectangle
from circle import Circle

if __name__ == "__main__":
    gl1 = LibraryV1()
    gl2 = LibraryV2()

    f1 = Rectangle(gl1, 1, 1, 2, 2)
    f1.draw()
    print()
    f1 = Circle(gl2, 2, 2, 4)
    f1.draw()
