class Vector3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return self.x + other.x, self.y + other.y, self.z + other.z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
