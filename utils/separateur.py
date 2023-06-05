class Separateur():
    """Fonction permettant de générer des séparateurs de contenu.

    Args:
        symbole (str, optional): Le symbole utilisé par défaut est "-".
        nombre (int, optional): La quantité de symboles répétés par défaut est 100.
        decorateur (str, optional): Le décorateur utilisé par défaut est "".

    Returns:
        str: Retourne un séparateur de type chaîne de caractères.
    """
    
    _symbole: str
    _nombre: int
    _decorateur: str
    
    def __init__(self, symbole: str = "-", nombre: int = 100, decorateur: str = "") -> None:
        self._symbole = symbole.strip()
        if nombre <= 0:
            self.nombre = 100
        else:
            self.nombre = int(nombre)
        self._decorateur = decorateur

    def afficher_separateur(self):
        if self._decorateur:
            print(f"{self._decorateur}{self._symbole * self.nombre}")
        else:
            print(f"{self._symbole * self.nombre}")