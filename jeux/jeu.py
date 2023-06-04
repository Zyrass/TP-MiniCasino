class Jeu:
    """Il s'agit d'une classe parente qui permet de définir le nom d'un jeu"""
    
    _game_name: str
    
    def __init__(self, game_name) -> None:
        self._game_name = game_name
        
    def bienvenue(self):
        print(f"Bienvenue dans {self._game_name}")