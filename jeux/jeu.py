class Jeu:
    """Il s'agit d'une classe parente qui permet de définir le nom d'un jeu."""
    
    _nom_jeu: str
    
    def __init__(self, nom_jeu) -> None:
        self._nom_jeu = nom_jeu
        
    def afficher_bienvenue(self):
        print(f"Bienvenue dans {self._nom_jeu}")
