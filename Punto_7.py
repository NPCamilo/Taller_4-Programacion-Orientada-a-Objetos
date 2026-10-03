\"""
Ejercicio 7
Cree una clase llamada Estudiante con:
- nombre
- codigo

Implemente el método __eq__ para que dos estudiantes sean iguales si tienen el mismo código.
Pruebe comparando varios objetos con ==.
\"""

class Estudiante:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __eq__(self, otro):
        if isinstance(otro, Estudiante):
            return self.codigo == otro.codigo
        return False

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


if __name__ == "__main__":
    e1 = Estudiante("Ana", "001")
    e2 = Estudiante("Andrea", "001")
    e3 = Estudiante("Luis", "002")
    print(e1 == e2)  # True
    print(e1 == e3)  # False
