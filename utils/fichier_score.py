class FichierScore:
    _nom_fichier: str
    _extension: str
    _scores: dict
    
    def __init__(self, nom_fichier: str, extension: str = "txt") -> None:
        self._nom_fichier = nom_fichier
        self._extension = extension
        self._scores = {}
        
    def get_nom_fichier(self) -> str:
        return self._nom_fichier
    
    def get_extension(self) -> str:
        return self._extension
        
    def initialisation_scores(self) -> dict:
        scores = self._scores
        nom_fichier_complet = f"{self._nom_fichier}.{self._extension}"
        try:
            with open(nom_fichier_complet, "r") as fichier:
                for ligne in fichier.readlines():
                    nom_joueur, score = ligne.strip().split(";")
                    scores[nom_joueur] = int(score)
        except FileNotFoundError:
            contenu_par_defaut = "GRESSIER;999\nALAIN;777\n"
            with open(nom_fichier_complet, "w") as fichier:
                fichier.write(contenu_par_defaut)
            scores = {
                "GRESSIER": 999,
                "ALAIN": 777
            }
        return scores
    
    def afficher_scores(self, nom_fichier_complet: str) -> None:
        scores = self.initialisation_scores()
        print("Tableau des scores:")
        with open(nom_fichier_complet, "r") as fichier:
            for ligne in fichier.readlines():
                nom_joueur, score = ligne.strip().split(";")
                solde = scores[nom_joueur]  # Utiliser le solde au lieu du score
                print(f"{nom_joueur} : {solde}€")
    
    def enregistrer_score(self, joueur, score: int) -> None:
        nom_fichier_complet = f"{self._nom_fichier}.{self._extension}"
        with open(nom_fichier_complet, "w") as fichier:
            for username, score in scores.items():
                fichier.write(f"{username.upper()};{score}\n")
