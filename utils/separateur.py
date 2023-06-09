class Separateur:
    def __init__(self, symbole: str = "-", nombre: int = 100, decorateur: str = "") -> None:
        self._symbole = symbole.strip()
        if nombre <= 0:
            self._nombre = 100
        else:
            self._nombre = int(nombre)
        self._decorateur = decorateur

    def afficher_separateur(self) -> None:
        if self._decorateur:
            print(f"{self._decorateur}{self._symbole * self._nombre}")
        else:
            print(f"{self._symbole * self._nombre}")
