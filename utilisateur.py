class Utilisateur:
    """Il s'agit d'une classe permettant d'initialiser un "utilisateur" en lui définissant un solde de départ de 100€ par défaut (modifiable). Cette classe dispose également de quelques méthodes qui lui sont propres."""

    _nom: str
    _score: int
    _solde: int

    def __init__(self, username: str, score: int = 0, solde: int = 100) -> None:
        """Initialise un utilisateur avec un nom, un score et un solde par défaut de 100€ s'il n'est pas spécifié.

        Args:
            username (str): Le nom du joueur.
            score (int, optional): Le score du joueur, par défaut 0.
            solde (int, optional): Le solde de départ du joueur, par défaut 100€.
        """
        self._nom = username
        self._score = score
        if solde <= 0:
            self._solde = 100
            print(f"Désolé, {self.get_nom()}, tu ne peux pas avoir un solde égal ou inférieur à 0€.")
            print("Attribution automatique de 100€ pour pouvoir jouer.")
        else:
            self._solde = solde

    def get_nom(self) -> str:
        """Retourne le nom de l'utilisateur."""
        return self._nom

    def afficher_score(self) -> str:
        """Retourne le score de l'utilisateur."""
        return f"Score: {self._score}"

    def afficher_solde(self) -> str:
        """Retourne le solde de l'utilisateur."""
        return f"Solde: {self._solde}€"

    def augmenter_solde(self, gains: int) -> None:
        """Augmente le solde de l'utilisateur.

        Args:
            gains (int): Le montant des gains à ajouter.
        """
        self._solde += gains

    def diminuer_solde(self, mise: int) -> None:
        """Diminue le solde de l'utilisateur.

        Args:
            mise (int): Le montant de la mise à déduire.
        """
        if mise <= self._solde:
            self._solde -= mise
            print(f"{self.get_nom()}, tu viens de miser {mise}€.")
        else:
            print(f"Désolé, {self.get_nom()}, tu n'as pas suffisamment d'argent pour miser {mise}€.")
