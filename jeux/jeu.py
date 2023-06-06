class Jeu:
    """Il s'agit d'une classe parente qui permet de définir le nom d'un jeu."""

    def __init__(self, nom_jeu: str) -> None:
        self._nom_jeu = nom_jeu

    def afficher_bienvenue(self) -> None:
        print(f"Bienvenue sur le jeu: \"La {self._nom_jeu.lower()}\"")