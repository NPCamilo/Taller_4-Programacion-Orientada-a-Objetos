\"""
Ejercicio 3
Cree una clase llamada Playlist que tenga:
- nombre_playlist
- canciones (lista)

Implemente el método __len__ para que al ejecutar:
len(mi_playlist)
se obtenga el número de canciones.

Pruebe agregando al menos 6 canciones.
\"""

class Playlist:
    def __init__(self, nombre_playlist):
        self.nombre_playlist = nombre_playlist
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def __len__(self):
        return len(self.canciones)


if __name__ == "__main__":
    mi_playlist = Playlist("Favoritas")
    mi_playlist.agregar_cancion("Bohemian Rhapsody")
    mi_playlist.agregar_cancion("Hotel California")
    mi_playlist.agregar_cancion("Imagine")
    mi_playlist.agregar_cancion("Stairway to Heaven")
    mi_playlist.agregar_cancion("Smells Like Teen Spirit")
    mi_playlist.agregar_cancion("Hey Jude")
    print(f"Nombre: {mi_playlist.nombre_playlist}")
    print(f"Número de canciones: {len(mi_playlist)}")
