from .jeu import Jeu
from ..utilisateurs import Utilisateur

class MachineASous(Jeu):
    
    def __init__(self):
        super().__init__("Machine à sous")
        
    def run(self, player: Utilisateur):
        from .check_files import check_machine_a_sous
        self.bienvenue()
        
        while True:
            print("\n + 1. Jouer 1€")
            print(" + 2. Jouer 2€")
            print(" + 3. Jouer 3€")
            print(" + 4. Jouer 4€")
            print(" + 5. Jouer 5€")
            print(" + Q. Quitter la machine à sous")
            print("")
            choix_joueur = input(f" {player._name}, fais un choix : ")
            
            if player._solde > 0:
                match choix_joueur:
                    case "1":
                        player.diminuer_solde(1)
                        check_machine_a_sous(player)
                    case "2":
                        player.diminuer_solde(2)
                        check_machine_a_sous(player)
                    case "3":
                        player.diminuer_solde(3)
                        check_machine_a_sous(player)
                    case "4":
                        player.diminuer_solde(4)
                        check_machine_a_sous(player)
                    case "5":
                        player.diminuer_solde(5)
                        check_machine_a_sous(player)
                    case "q":
                        break
                    case _:
                        print("... choix non valide, veuillez réessayer.")
    
            else:
                print(f"\n GAME OVER pour {player._name}, tu n'as plus un sou en poche.\n")
                break
