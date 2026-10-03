\"""
Ejercicio 9
Cree una clase llamada Biblioteca que contenga:
- lista de libros

Implemente:
- __len__ → cantidad de libros
- __add__ → permitir unir dos bibliotecas.
La nueva biblioteca debe contener todos los libros de ambas.
\"""

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"\"{self.titulo}\" escrito por {self.autor}"


class Biblioteca:
    def __init__(self, nombre="Biblioteca"):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def __len__(self):
        return len(self.libros)

    def __add__(self, otra):
        if isinstance(otra, Biblioteca):
            nueva_biblioteca = Biblioteca(f"{self.nombre} + {otra.nombre}")
            nueva_biblioteca.libros = self.libros + otra.libros
            return nueva_biblioteca
        return NotImplemented

    def __str__(self):
        if not self.libros:
            return f"{self.nombre} está vacía"
        resultado = f"{self.nombre} - Libros:\n"
        for i, libro in enumerate(self.libros, 1):
            resultado += f"{i}. {libro}\n"
        return resultado


if __name__ == "__main__":
    b1 = Biblioteca("Biblioteca A")
    b1.agregar_libro(Libro("El principito", "Antoine de Saint-Exupéry"))
    b1.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez"))

    b2 = Biblioteca("Biblioteca B")
    b2.agregar_libro(Libro("Don Quijote de la Mancha", "Miguel de Cervantes"))
    b2.agregar_libro(Libro("Rayuela", "Julio Cortázar"))

    b3 = b1 + b2
    print(f"Total libros en b3: {len(b3)}")
    print(b3)
