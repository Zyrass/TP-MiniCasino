from .separateur import Separateur
from jeux.machine_a_sous import MachineASous
from jeux.roulette import Roulette


class Menu(Separateur):
    def __init__(self):
        super().__init__("-", 69, "+ ")
        self._titre = "+ 📍 MENU - MINI CASINO"
        self._choix_1 = "+ 1. ➡️   Machine à sous"
        self._choix_2 = "+ 2. ➡️   Roulette"
        self._quitter = "+ Q. ⏹️   Quitter le mini casino"

    def afficher_titre(self) -> None:
        print(self._titre)

    def afficher_choix_1(self) -> None:
        print(self._choix_1)

    def afficher_choix_2(self) -> None:
        print(self._choix_2)

    def afficher_quitter(self) -> None:
        print(self._quitter)

    def afficher_menu(self, joueur, fichier_scores) -> None:
        while True:
            self.afficher_separateur()
            self.afficher_titre()
            self.afficher_separateur()
            self.afficher_choix_1()
            self.afficher_choix_2()
            self.afficher_separateur()
            self.afficher_quitter()
            self.afficher_separateur()

            choix_utilisateur = input(
                f"\n{joueur.nom.strip().capitalize()}, veuillez saisir un choix: ")
            print("\n")

            if choix_utilisateur == "1":
                machine = MachineASous()
                machine.run(joueur)
            elif choix_utilisateur == "2":
                roulette = Roulette()
                roulette.run(joueur)
            elif choix_utilisateur.lower() == "q":
                joueur.enregistrer_nouveau_solde(fichier_scores)
                print(f"Au revoir {joueur.nom}, à bientôt j'espère.\n")
                fichier_scores.afficher_scores(fichier_scores.lire_scores())
                break
            else:
                print(
                    f"Désolé {joueur.nom.strip().capitalize()}, ce choix est invalide, veuillez réessayer.\n")
