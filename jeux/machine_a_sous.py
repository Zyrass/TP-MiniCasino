from .jeu import Jeu
from utilisateur import Utilisateur

class MachineASous(Jeu):
    
    def __init__(self):
        super().__init__("Machine à sous")
        
    def run(self, joueur: Utilisateur):
        from ..utils.common import Utilitaires
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
