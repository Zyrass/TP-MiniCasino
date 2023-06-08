from utils.separateur import Separateur
from random import randint
from os import system


class MachineASous(Separateur):
    def __init__(self):
        super().__init__("-", 69, "+ ")

    def afficher_titre(self) -> None:
        print("+ ---------------------------------------------------------------------")
        print("+ 🕹️  Machine à sous")
        print("+ ---------------------------------------------------------------------")

    def afficher_choix(self) -> None:
        print("+ 1. ➡️  Jouer 1€ -  🪙")
        print("+ 2. ➡️  Jouer 2€ -  🪙 🪙")
        print("+ 3. ➡️  Jouer 3€ -  🪙 🪙 🪙")
        print("+ 4. ➡️  Jouer 4€ -  🪙 🪙 🪙 🪙")
        print("+ 5. ➡️  Jouer 5€ -  🪙 🪙 🪙 🪙 🪙")
        print("+ ---------------------------------------------------------------------")
        print("+ 6. 🔧 - TEST DEBUG - Jouer 100€")
        print("+ ---------------------------------------------------------------------")
        print("+ Q. ⏹️  Revenir sur la sélection des jeux du casino")
        print("+ ---------------------------------------------------------------------")

    def run(self, joueur) -> None:
        separateur_machine_a_sous = Separateur("-", 69, "+ ")

        separateur_machine_a_sous.afficher_separateur()
        self.afficher_titre()
        separateur_machine_a_sous.afficher_separateur()
        self.afficher_choix()
        separateur_machine_a_sous.afficher_separateur()

        while True:
            choix_utilisateur = input(
                f"\n{joueur.nom.strip().capitalize()}, veuillez saisir un choix: ")
            print("\n")

            if choix_utilisateur == "1":
                self.jouer(joueur, 1)
            elif choix_utilisateur == "2":
                self.jouer(joueur, 2)
            elif choix_utilisateur == "3":
                self.jouer(joueur, 3)
            elif choix_utilisateur == "4":
                self.jouer(joueur, 4)
            elif choix_utilisateur == "5":
                self.jouer(joueur, 5)
            elif choix_utilisateur == "6":
                self.jouer(joueur, 100)
            elif choix_utilisateur.lower() == "q":
                print(f"Retour au menu principal.\n")
                break
            else:
                print(
                    f"Désolé {joueur.nom.strip().capitalize()}, ce choix est invalide, veuillez réessayer.\n")

    def jouer(self, joueur, mise) -> None:
        if mise > joueur.solde:
            print(f"{joueur.nom}, tu n'as pas assez d'argent pour miser {mise}€.\n")
            return

        symboles = ["❌", "💲", "💎", "🍀", "💰", "🪙"]
        symbole_1 = symboles[randint(0, 5)]
        symbole_2 = symboles[randint(0, 5)]
        symbole_3 = symboles[randint(0, 5)]

        separateur_machine_a_sous = Separateur("-", 69, "+ ")

        separateur_machine_a_sous.afficher_separateur()
        print(f"+ {symbole_1}  {symbole_2}  {symbole_3}")
        separateur_machine_a_sous.afficher_separateur()

        if symbole_1 == symbole_2 == symbole_3:
            if symbole_1 == "❌":
                gains = 0
            elif symbole_1 == "🍀":
                gains = mise * 20
            elif symbole_1 == "💲":
                gains = mise * 40
            elif symbole_1 == "💰":
                gains = mise * 80
            elif symbole_1 == "💎":
                gains = 500
            else:
                gains = mise * 160

            joueur.augmenter_solde(gains)
            print(
                f"+ Félicitations {joueur.nom.strip().capitalize()} ! Tu as gagné {gains}€.")
            print(f"+ Tu as dorénavant {joueur.solde}€ en poche !!")
            separateur_machine_a_sous.afficher_separateur()
            print()
        else:
            joueur.diminuer_solde(mise)
            print(
                f"+ Dommage {joueur.nom.strip().capitalize()}, tu as perdu {mise}€.")
            print(f"+ Il ne te reste que {joueur.solde}€ en poche...")
            separateur_machine_a_sous.afficher_separateur()
            print()
