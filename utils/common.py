from random import randint
from ..jeux.machine_a_sous import MachineASous
from ..jeux.roulette import Roulette
from ..utilisateur import Utilisateur

from .separateur import Separateur

separateur_tirets_x100_avec_decorateur_plus: Separateur = Separateur("-", 100, " + ")
separateur_tirets_x35_avec_decorateur_plus: Separateur = Separateur("-", 35, " + ")

class Utilitaires:

    def afficher_menu(self, joueur: Utilisateur):
        while True:
            self.separateur("-", 35)
            print(" + MENU - MINI CASINO")
            self.separateur("-", 35)
            print(" + 1. Machine à sous")
            print(" + 2. Roulette")
            self.separateur("-", 35)
            print(" + Q. Quitter le mini casino")
            self.separateur("-", 35)

            choix_utilisateur = input(f"\n{joueur.get_nom().strip().capitalize()}, veuillez saisir un choix: ")
            self.espace()

            if choix_utilisateur == "1":
                machine = MachineASous()
                machine.run(joueur)
            elif choix_utilisateur == "2":
                roulette = Roulette()
                roulette.run(joueur)
            elif choix_utilisateur.lower() == "q":
                # Sauvegarde de la nouvelle valeur du solde du joueur
                self.scores[joueur.get_nom()] = joueur.get_solde()
                self.nouveau_scores(joueur.get_nom(), joueur.get_solde())
                break
            else:
                print("\n Désolé, ce choix est invalide, veuillez réessayer.\n")
                self.espace()

    def verification_machine_a_sous(self, joueur: Utilisateur):
        resultat = [randint(1,6) for _ in range(3)]
        print(f" Résultats : {resultat}")
        print(f" {joueur.get_nom().capitalize()}, il te reste actuellement: {joueur.get_solde()}€")
        
        if resultat[0] == resultat[1] == resultat[2]:
            print(" Félicitations, vous avez gagné 500€")
            joueur.increment_solde(500)
        else:
            print(" Désolé, vous avez perdu. Essayez encore !")
