\"""
Ejercicio 4
Cree una clase llamada EquipoFutbol con:
- nombre_equipo
- jugadores (lista)

Implemente __len__ para que al usar len() se obtenga la cantidad de jugadores del equipo.

Luego cree dos equipos y muestre cuántos jugadores tiene cada uno.
\"""

class EquipoFutbol:
    def __init__(self, nombre_equipo):
        self.nombre_equipo = nombre_equipo
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def __len__(self):
        return len(self.jugadores)


if __name__ == "__main__":
    equipo1 = EquipoFutbol("Real Madrid")
    equipo1.agregar_jugador("Benzema")
    equipo1.agregar_jugador("Modrić")
    equipo1.agregar_jugador("Vinicius Jr.")

    equipo2 = EquipoFutbol("Barcelona")
    equipo2.agregar_jugador("Messi")
    equipo2.agregar_jugador("Xavi")
    equipo2.agregar_jugador("Iniesta")
    equipo2.agregar_jugador("Piqué")

    print(f"{equipo1.nombre_equipo}: {len(equipo1)} jugadores")
    print(f"{equipo2.nombre_equipo}: {len(equipo2)} jugadores")
