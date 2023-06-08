from .separateur import Separateur
from jeux.machine_a_sous import MachineASous
from jeux.roulette import Roulette
from os import system


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
        
    def menu_contenu(self, joueur)-> str:
        self.afficher_separateur()
        self.afficher_titre()
        self.afficher_separateur()
        self.afficher_choix_1()
        self.afficher_choix_2()
        self.afficher_separateur()
        self.afficher_quitter()
        self.afficher_separateur()
        choix_utilisateur = input(
                f"\n🖊️ - {joueur.nom.strip().capitalize()}, veuillez saisir un choix: ")
        return choix_utilisateur

    def afficher_menu(self, joueur, fichier_scores) -> None:
        while True:
            choix_utilisateur = self.menu_contenu(joueur)
            if choix_utilisateur == "1":
                system("clear")
                print()
                machine = MachineASous()
                machine.run(joueur)
            elif choix_utilisateur == "2":
                system("clear")
                print()
                roulette = Roulette()
                roulette.run(joueur)
            elif choix_utilisateur.lower() == "q":
                system("clear")
                joueur.enregistrer_nouveau_solde(fichier_scores)
                print(f"\nJe suis navré de te voir partir {joueur.nom}, à bientôt je l'espère.")
                print("Avant que tu ne partes, je tiens à te montrer l'état actuel du tableau des scores")
                print("Peut-être que tu auras détrôné les meilleurs joueurs 😉\n")
                fichier_scores.afficher_scores(fichier_scores.lire_scores())
                break
            else:
                system("clear")
                print(
                    f"\n⛔ - Désolé {joueur.nom.strip().capitalize()}, ce choix est invalide, veuillez réessayer.\n")
