from random import randint
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
            system("clear")
            print("\n")
            self.afficher_separateur()
            print(f"+ {self._nom_jeu}")
            self.afficher_separateur()
            print("+ 1. Jouer 1€")
            print("+ 2. Jouer 2€")
            print("+ 3. Jouer 3€")
            print("+ 4. Jouer 4€")
            print("+ 5. Jouer 5€")
            self.afficher_separateur()
            print("+ 6. TEST DEBUG - Jouer 100€")
            self.afficher_separateur()
            print("+ Q. Revenir sur la sélection des jeux du casino")
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
                    system("clear")
                    return
                else:
                    print("... choix non valide, veuillez réessayer.")
            elif joueur._solde == 0:
                print(f"GAME OVER pour {joueur.get_nom()}, tu n'as plus un sou en poche.\n")
                touche_appuyer = input("Appuyer sur une touche pour revenir au menu précédent")
                if len(touche_appuyer) > 0:
                    break

    def verification_machine_a_sous(self, joueur):
        resultat = [randint(1,6) for _ in range(3)]
        print(f"\nRésultat du tirage : {resultat}")
        
        if resultat[0] == resultat[1] == resultat[2]:
            print("Super félicitation, vous venez de gagner 500€ cash\n")
            joueur.augmenter_solde(500)
        else:
            print("Dommage, vous avez perdu. Essayez encore !\n")
