\"""
Ejercicio 10
Cree una clase llamada Curso con:
- nombre_curso
- estudiantes (lista de objetos Estudiante)

Implemente:
- __len__ → cantidad de estudiantes
- __str__ → mostrar lista de estudiantes
- __eq__ → dos cursos son iguales si tienen el mismo número de estudiantes.

Pruebe:
len(curso1)
print(curso1)
curso1 == curso2
\"""

class Estudiante:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def __len__(self):
        return len(self.estudiantes)

    def __str__(self):
        if not self.estudiantes:
            return f"Curso {self.nombre_curso} sin estudiantes"
        resultado = f"Curso: {self.nombre_curso}\nEstudiantes:\n"
        for i, est in enumerate(self.estudiantes, 1):
            resultado += f"{i}. {est}\n"
        return resultado

    def __eq__(self, otro):
        if isinstance(otro, Curso):
            return len(self) == len(otro)
        return False


if __name__ == "__main__":
    curso1 = Curso("Programación IV")
    curso1.agregar_estudiante(Estudiante("Ana", "001"))
    curso1.agregar_estudiante(Estudiante("Luis", "002"))
    curso1.agregar_estudiante(Estudiante("María", "003"))

    curso2 = Curso("Bases de Datos")
    curso2.agregar_estudiante(Estudiante("Carlos", "010"))
    curso2.agregar_estudiante(Estudiante("Sofía", "011"))
    curso2.agregar_estudiante(Estudiante("Pedro", "012"))

    curso3 = Curso("Redes")
    curso3.agregar_estudiante(Estudiante("Andrés", "020"))
    curso3.agregar_estudiante(Estudiante("Laura", "021"))

    print(f"Cantidad curso1: {len(curso1)}")
    print(curso1)
    print(f"curso1 == curso2: {curso1 == curso2}")
    print(f"curso1 == curso3: {curso1 == curso3}")
