from ..utilisateur import Utilisateur

class fichierScore:
    
    _nom_fichier: str
    _extension: str
    _scores: dict = {}
    
    def __init__(self, nom_fichier: str, extension: str = "txt") -> None:
        self._nom_fichier = nom_fichier
        self._extension = extension
        
    def get_nom_fichier(self):
        return self._nom_fichier
    
    def get_extension(self):
        return self._extension
        
    def initialisation_scores(self):
        """Initialiser le fichier score.txt.

        Returns:
            dict: Dictionnaire des scores {username: score}.
        """
        scores = self._scores
        nom_fichier_complet = f"{self._nom_fichier}.{self._extension}"
        try:
            with open(nom_fichier_complet, "r") as fichier:
                for ligne in fichier.readlines():
                    nom_joueur, score = ligne.strip().split(";")
                    scores[nom_joueur] = int(score)
        except FileNotFoundError:
            contenu_par_defaut = "GRESSIER;999\nGUILLON;777\n"
            with open(nom_fichier_complet, "w") as fichier:
                fichier.write(contenu_par_defaut)
                scores = {
                    "GRESSIER": 999,
                    "GUILLON": 777
                }
        return scores
    
    def enregistrer_score(self, joueur: Utilisateur, score: int):
        """Ajoute un nouveau score à la suite.

        Args:
            username (str): Le nom de l'utilisateur.
            score (int): Le score de l'utilisateur.
        """
        # Chargement des scores existants
        scores = self.initialisation_scores()

        scores[joueur.get_nom()] = score

        nom_fichier_complet = f"{self._nom_fichier}.{self._extension}"
        with open(nom_fichier_complet, "w") as fichier:
            for username, score in scores.items():
                fichier.write(f"{username.upper()};{score}\n")
