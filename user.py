class User:
    """Il s'agit d'une classe permettant d'initialiser un "utilisateur" en lui définissant un solde de départ de 100€ par défaut. (modifiable)\nÉgalement elle dispose de 2 méthodes qui permet à l'utilisateur d'incrémenter et de décrémenter son solde.
    """
    
    _name: str
    _solde: int
    
    def __init__(self, username: str, solde: int = 100) -> None:
        """_summary_

        Args:
            username (str): Le nom du joueur
            solde (int, optional): Le solde de départ du joueur, par défaut si non saisie, il sera de 100€
        """
        self._name = username
        if solde <= 0:
            self._solde = 100
            print(f"Désolé, {self._name}, tu ne pouvais pas avoir un solde égale ou inférieur à 0.\nJe t'ai ainsi attribuer 100€ par défaut.")
        else:
            self._solde = solde
        
    def increment_solde(self, gains: int) -> None:
        """Permet d'incrémenter le solde du joueur
        
        Args:
            gains (int): Il s'agit d'un nombre entier
        """
        self._solde += gains
        
    def decrement_solde(self, pertes: int) -> None:
        """Permet de décrémenter le solde du joueur
        
        Args:
            pertes (int): Il s'agit d'un nombre entier qui est retiré de son solde.
        """
        # Contrôle pour que la pertes soit bien inférieur ou égale au solde du joueur 
        if pertes <= self._solde:
            self._solde -= pertes
        