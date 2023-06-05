from random import randint
from .jeu import Jeu
from utils.common import *

class MachineASous(Jeu):
    
    def __init__(self):
        super().__init__("Machine à sous")
        
    def run(self, joueur):
        super().afficher_bienvenue()
        
        continuer = True
        while continuer:
            print("\n + 1. Jouer 1€")
            print(" + 2. Jouer 2€")
            print(" + 3. Jouer 3€")
            print(" + 4. Jouer 4€")
            print(" + 5. Jouer 5€")
            print(" + Q. Revenir au menu précédent")
            print("")
            choix_joueur = input(f" {joueur.get_nom()}, fais un choix : ")
            
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
                elif choix_joueur.lower() == "q":
                    #   continuer = False
                    break
                else:
                    print("... choix non valide, veuillez réessayer.")
            else:
                print(f"\n GAME OVER pour {joueur.get_nom()}, tu n'as plus un sou en poche.\n")
                break

    def verification_machine_a_sous(self, joueur):
        resultat = [randint(1,6) for _ in range(3)]
        print(f" Résultats : {resultat}")
        print(f" {joueur.get_nom().capitalize()}, il te reste actuellement: {joueur._solde}€")
        
        if resultat[0] == resultat[1] == resultat[2]:
            print(" Félicitations, vous avez gagné 500€")
            joueur.augmenter_solde(500)
        else:
            print(" Désolé, vous avez perdu. Essayez encore !")
