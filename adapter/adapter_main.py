from point import Point
from line import Line
from square import Square
from circle import Circle


if __name__ == "__main__":
    figures_list = [Point(), Line(), Square(), Circle()]

    for figure in figures_list:
        figure.show()
