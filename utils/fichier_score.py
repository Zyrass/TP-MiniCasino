class FichierScore:
    def __init__(self):
        self._nom_fichier = "scores.txt"

    def lire_scores(self):
        scores = {}
        nom_fichier_complet = self._nom_fichier
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

    def afficher_scores(self, scores):
        top_3_scores = sorted(
            scores.items(), key=lambda x: x[1], reverse=True)[:3]

        print("Tableau des scores :")
        for i, (nom_joueur, score_joueur) in enumerate(top_3_scores, start=1):
            if i == 1:
                print(f"🥇 {nom_joueur} - {score_joueur}€")
            elif i == 2:
                print(f"🥈 {nom_joueur} - {score_joueur}€")
            elif i == 3:
                print(f"🥉 {nom_joueur} - {score_joueur}€")
            else:
                print(f"{nom_joueur} - {score_joueur}€")

    def enregistrer_nouveau_score(self, nom_joueur, nouveau_score):
        scores = self.lire_scores()

        if nom_joueur in scores:
            scores[nom_joueur] = nouveau_score
        else:
            scores[nom_joueur] = nouveau_score

        with open(self._nom_fichier, "w") as fichier:
            for nom, score in scores.items():
                ligne = f"{nom};{score}\n"
                fichier.write(ligne)
