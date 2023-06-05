from random import randint
from .jeu import Jeu
from utils.common import Separateur

class MachineASous(Jeu):
    
    def __init__(self):
        super().__init__("Machine à sous")
        
    def run(self, joueur):
        self.bienvenue()
        
        while True:
            print("\n + 1. Jouer 1€")
            print(" + 2. Jouer 2€")
            print(" + 3. Jouer 3€")
            print(" + 4. Jouer 4€")
            print(" + 5. Jouer 5€")
            print(" + Q. Quitter la machine à sous")
            print("")
            choix_joueur = input(f" {joueur.get_nom()}, fais un choix : ")
            
            if joueur.get_solde() > 0:
                match choix_joueur:
                    case "1":
                        joueur.diminuer_solde(1)
                        Utilitaires.verification_machine_a_sous(joueur)
                    case "2":
                        joueur.diminuer_solde(2)
                        Utilitaires.verification_machine_a_sous(joueur)
                    case "3":
                        joueur.diminuer_solde(3)
                        Utilitaires.verification_machine_a_sous(joueur)
                    case "4":
                        joueur.diminuer_solde(4)
                        Utilitaires.verification_machine_a_sous(joueur)
                    case "5":
                        joueur.diminuer_solde(5)
                        Utilitaires.verification_machine_a_sous(joueur)
                    case "q":
                        break
                    case _:
                        print("... choix non valide, veuillez réessayer.")
    
            else:
                print(f"\n GAME OVER pour {joueur.get_nom()}, tu n'as plus un sou en poche.\n")
                break

    def verification_machine_a_sous(self, joueur):
        resultat = [randint(1,6) for _ in range(3)]
        print(f" Résultats : {resultat}")
        print(f" {joueur.get_nom().capitalize()}, il te reste actuellement: {joueur.get_solde()}€")
        
        if resultat[0] == resultat[1] == resultat[2]:
            print(" Félicitations, vous avez gagné 500€")
            joueur.increment_solde(500)
        else:
            print(" Désolé, vous avez perdu. Essayez encore !")
