class Joueur:
    def __init__(self, nom: str, solde: int = 100, score: int = 0):
        self._nom = nom
        self._solde = solde
        self._score = score

    @property
    def nom(self) -> str:
        return self._nom

    @property
    def solde(self) -> int:
        return self._solde

    def diminuer_solde(self, mise: int) -> None:
        if mise <= self._solde:
            self._solde -= mise
            print(f"{self._nom}, tu viens de miser {mise}€.")

    def augmenter_solde(self, gains: int) -> None:
        self._solde += gains

    def enregistrer_nouveau_solde(self, fichier_scores) -> None:
        fichier_scores.enregistrer_nouveau_score(self.nom, self.solde)

    def afficher_score(self) -> None:
        print(f"Score: {self._score}")
