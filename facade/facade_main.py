from vector_2d import Vector2D
from vector_3d import Vector3D

if __name__ == "__main__":
    print("Operations on: Vector3D")
    v3_1 = Vector3D(1, 2, 3)
    v3_2 = Vector3D(8, 7, 6)
    print(f"{v3_1} + {v3_2} = Vector3D{v3_1 + v3_2}")
    print(f"{v3_1} + {Vector3D(1, 2, 3)} = Vector3D{v3_1 + Vector3D(1, 2, 3)}")

    print('_' * 16)
    print("Operations on: Vector2D")
    v2_1 = Vector2D(1, 2)
    v2_2 = Vector2D(8, 7)
    print(f"{v2_1} + {v2_2} = Vector2D{v2_1 + v2_2}")
    print(f"{v2_1} + {Vector2D(1, 2)} = Vector2D{v2_1 + Vector2D(1, 2)}")
