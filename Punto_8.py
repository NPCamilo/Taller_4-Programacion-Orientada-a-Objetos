\"""
Ejercicio 8
Cree una clase llamada CarritoCompras que tenga:
- productos (lista)

Implemente:
- __len__ → cantidad de productos
- __str__ → mostrar todos los productos del carrito.
\"""

class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def __len__(self):
        return len(self.productos)

    def __str__(self):
        if not self.productos:
            return "El carrito está vacío"
        resultado = "Carrito de compras:\n"
        for i, prod in enumerate(self.productos, 1):
            resultado += f"{i}. {prod}\n"
        return resultado


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}: "


if __name__ == "__main__":
    carrito = CarritoCompras()
    carrito.agregar_producto(Producto("Laptop", 2500000))
    carrito.agregar_producto(Producto("Mouse", 150000))
    carrito.agregar_producto(Producto("Teclado", 300000))
    print(f"Cantidad: {len(carrito)}")
    print(carrito)
