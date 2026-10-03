\"""
Ejercicio 6
Cree una clase llamada Vector2D con:
- x
- y

Implemente el método __add__ para que al sumar dos vectores se obtenga un nuevo vector.
Ejemplo: (2,3) + (4,1) = (6,4).
\"""

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        if isinstance(otro, Vector2D):
            nuevo_x = self.x + otro.x
            nuevo_y = self.y + otro.y
            return Vector2D(nuevo_x, nuevo_y)
        return NotImplemented

    def __str__(self):
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    v1 = Vector2D(2, 3)
    v2 = Vector2D(4, 1)
    v3 = v1 + v2
    print(f"{v1} + {v2} = {v3}")
