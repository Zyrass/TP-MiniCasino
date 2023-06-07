from random import randint
from utils.fichier_score import FichierScore
from jeux.jeu import Jeu
from utils.separateur import Separateur
from os import system


class MachineASous(Jeu, Separateur):

    def __init__(self):
        Jeu.__init__(self, "Machine à sous")
        Separateur.__init__(self, "-", 69, "+ ")

    def run(self, joueur):
        system("clear")
        print("\n")
        self.afficher_bienvenue()
        print("\n")
        while True:
            self.afficher_separateur()
            print(f"+ 🕹️  {self._nom_jeu}")
            self.afficher_separateur()
            print("+ 1. ➡️  Jouer 1€ -  🪙")
            print("+ 2. ➡️  Jouer 2€ -  🪙 🪙")
            print("+ 3. ➡️  Jouer 3€ -  🪙 🪙 🪙")
            print("+ 4. ➡️  Jouer 4€ -  🪙 🪙 🪙 🪙")
            print("+ 5. ➡️  Jouer 5€ -  🪙 🪙 🪙 🪙 🪙")
            self.afficher_separateur()
            print("+ 6. 🔧 - TEST DEBUG - Jouer 100€")
            self.afficher_separateur()
            print("+ Q. ⏹️  Revenir sur la sélection des jeux du casino")
            self.afficher_separateur()
            print(f"\n{joueur.get_nom()}, tu disposes de {joueur._solde}€")
            choix_joueur = input(f"fais un choix : ")

            if joueur._solde > 0:
                if choix_joueur == "1":
                    joueur.diminuer_solde(1)
                    self.verification_machine_a_sous(joueur)
                elif choix_joueur == "2":
                    joueur.diminuer_solde(2)
                    self.verification_machine_a_sous(joueur)
                elif choix_joueur == "3":
                    joueur.diminuer_solde(3)
                    self.verification_machine_a_sous(joueur)
                elif choix_joueur == "4":
                    joueur.diminuer_solde(4)
                    self.verification_machine_a_sous(joueur)
                elif choix_joueur == "5":
                    joueur.diminuer_solde(5)
                    self.verification_machine_a_sous(joueur)
                elif choix_joueur == "6":
                    joueur.diminuer_solde(100)
                    self.verification_machine_a_sous(joueur)
                elif choix_joueur.lower() == "q":
                    FichierScore.enregistrer_score("scores.txt", joueur, joueur._solde)
                    system("clear")
                    return
                else:
                    print("... choix non valide, veuillez réessayer.")
            elif joueur._solde == 0:
                print(
                    f" ❌ - GAME OVER pour {joueur.get_nom()}, tu n'as plus de 🪙 en poche.\n")
                FichierScore.enregistrer_score("scores.txt", joueur, joueur._solde)
                break

    def verification_machine_a_sous(self, joueur):
        separateur_validation = Separateur("=", 100, "+ ")
        resultat = [randint(1, 6) for _ in range(3)]
        print("\n")
        separateur_validation.afficher_separateur()
        print(f"+ Résultat du tirage : {resultat}")
        separateur_validation.afficher_separateur()
        if resultat[0] == resultat[1] == resultat[2]:
            print("+ ✅ - Super félicitation, vous venez de gagner 500€ cash")
            separateur_validation.afficher_separateur()
            print()
            joueur.augmenter_solde(500)
        else:
            print("+ ❌ - Dommage, vous avez perdu. Essayez encore !")
        separateur_validation.afficher_separateur()
        print()
            

