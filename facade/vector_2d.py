from vector_3d import Vector3D


class Vector2D(object):
    def __init__(self, x, y):
        self.vector = Vector3D(x, y, 0)

    def __add__(self, other):
        x, y, z = self.vector + other.vector
        return x, y

    def __str__(self):
        return f"Vector2D({self.vector.x}, {self.vector.y})"
