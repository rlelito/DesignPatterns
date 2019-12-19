from picture import Picture
from line import Line
from rectangle import Rectangle
from text import Text


if __name__ == "__main__":
    graphic = Picture()
    graphic.add(Line())
    graphic.add(Rectangle())

    graphic_sub = Picture()
    graphic_sub.add(Text())
    graphic_sub.add(Line())
    graphic_sub.add(Rectangle())

    graphic.add(graphic_sub)
    graphic.add(Line())

    graphic.draw()
