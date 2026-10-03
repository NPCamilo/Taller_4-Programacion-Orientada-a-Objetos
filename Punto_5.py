\"""
Ejercicio 5
Cree una clase llamada Producto con:
- nombre
- precio

Implemente el método __add__ para que al sumar dos productos se obtenga la suma de sus precios.
\"""

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __add__(self, otro):
        if isinstance(otro, Producto):
            return self.precio + otro.precio
        return NotImplemented

    def __str__(self):
        return f"{self.nombre}: "


if __name__ == "__main__":
    p1 = Producto("Laptop", 2500000)
    p2 = Producto("Mouse", 150000)
    print(f"Suma de precios: ")
