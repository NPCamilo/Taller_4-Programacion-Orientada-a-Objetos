\"""
Ejercicio 1
Cree una clase llamada Persona con los atributos:
- nombre
- edad

Implemente el método __str__ para que al imprimir el objeto se muestre:
Nombre: Carlos - Edad: 25

Luego cree 3 objetos y muéstrelos usando print().
\"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad}"


if __name__ == "__main__":
    p1 = Persona("Carlos", 25)
    p2 = Persona("Ana", 22)
    p3 = Persona("Luis", 30)
    print(p1)
    print(p2)
    print(p3)
