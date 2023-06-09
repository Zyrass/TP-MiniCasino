from utils.separateur import Separateur
from random import choice
from os import system


class Roulette(Separateur):
    def __init__(self):
        super().__init__("-", 100, "+ ")

    def afficher_titre(self) -> None:
        print("+ ---------------------------------------------------------------------")
        print("+ 🎲 Roulette")
        print("+ ---------------------------------------------------------------------")

    def afficher_choix(self) -> None:
        print("+ 1. ➡️  Jouer 1€ sur un nombre")
        print("+ 2. ➡️  Jouer 2€ sur une couleur (🔴 ou ⚫)")
        print("+ 3. ➡️  Jouer 3€ sur un nombre pair ou impair")
        print("+ 4. ➡️  Jouer 4€ sur un groupe de nombres (1-12, 13-24, 25-36)")
        print("+ 5. ➡️  Jouer 5€ sur une douzaine (1-12, 13-24, 25-36)")
        print("+ ---------------------------------------------------------------------")
        print("+ Q. ⏹️  Revenir sur la sélection des jeux du casino")
        print("+ ---------------------------------------------------------------------")

    def menu_content(self):
        separateur_roulette = Separateur("-", 100, "+ ")

        separateur_roulette.afficher_separateur()
        self.afficher_titre()
        separateur_roulette.afficher_separateur()
        self.afficher_choix()
        separateur_roulette.afficher_separateur()
        
    def tapis_de_jeu_un_nombre(self):
        separateur_roulette = Separateur("-", 110, "+ ")
        separateur_roulette.afficher_separateur()
        print("+ \t 0\t 1\t 2\t 3\t 4\t 5\t 6\t 7\t 8\t 9\t10\t11\t12")
        separateur_roulette.afficher_separateur()
        print("+ \t13\t14\t15\t16\t17\t18\t19\t20\t21\t22\t23\t24")
        separateur_roulette.afficher_separateur()
        print("+ \t25\t26\t27\t28\t29\t30\t31\t32\t33\t34\t35\t36")
        separateur_roulette.afficher_separateur()

    def run(self, joueur) -> None:
        self.menu_content()
        while True:
            print(f"\nTu disposes de {joueur.solde}€ en poche...")
            choix_utilisateur = input(
                f"{joueur.nom.strip().capitalize()}, veuillez saisir un choix: ")
            print("\n")

            if choix_utilisateur == "1":
                system("clear")
                print("\n ℹ️  - Choisis un seul nombre sur le tapis de jeu suivant :\n")
                self.jouer_sur_nombre(joueur, 1)
            elif choix_utilisateur == "2":
                system("clear")
                print()
                self.menu_content()
                self.jouer_sur_couleur(joueur, 2)
            elif choix_utilisateur == "3":
                system("clear")
                print()
                self.menu_content()
                self.jouer_sur_parite(joueur, 3)
            elif choix_utilisateur == "4":
                system("clear")
                print()
                self.menu_content()
                self.jouer_sur_groupe(joueur, 4)
            elif choix_utilisateur == "5":
                system("clear")
                print()
                self.menu_content()
                self.jouer_sur_douzaine(joueur, 5)
            elif choix_utilisateur.lower() == "q":
                print(f"Retour au menu principal.\n")
                break
            else:
                print(
                    f"Désolé {joueur.nom.strip().capitalize()}, ce choix est invalide, veuillez réessayer.\n")

    def jouer_sur_nombre(self, joueur, mise) -> None:
        if mise > joueur.solde:
            print(f"\n ⛔ - {joueur.nom}, tu n'as pas assez d'argent pour miser {mise}€.\n")
            return

        self.tapis_de_jeu_un_nombre()

        numero_gagnant = choice(range(37))

        if int(input("\n🖊️ - Choisissez un numéro entre 0 et 36 : ")) == numero_gagnant:
            gains = mise * 36
            joueur.augmenter_solde(gains)
            print(f"\n👀 - Le numéro gagnant est : {numero_gagnant}")
            print(f"🎉 - Félicitations {joueur.nom.strip().capitalize()} ! Tu as gagné {gains}€.\n")
        else:
            joueur.diminuer_solde(mise)
            print(f"\n👀 - Le numéro gagnant est : {numero_gagnant}")
            print(f"❌ - Dommage {joueur.nom.strip().capitalize()}, tu as perdu {mise}€.\n")


    def jouer_sur_couleur(self, joueur, mise) -> None:
        if mise > joueur.solde:
            print(f"{joueur.nom}, tu n'as pas assez d'argent pour miser {mise}€.\n")
            return

        separateur_roulette = Separateur("-", 69, "+ ")
        separateur_roulette.afficher_separateur()
        print("+ 🔴     : 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36")
        print("+ ⚫      : 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35")
        separateur_roulette.afficher_separateur()

        couleur_gagnante = choice(["🔴", "⚫"])

        choix_couleur = input("Choisissez une couleur (🔴 (r) / ⚫ (n)) : ").lower()
        if choix_couleur == 'r':
            choix_couleur = '🔴'
        elif choix_couleur == 'n':
            choix_couleur = '⚫'

        print(f"\nLa couleur gagnante est : {couleur_gagnante}\n")

        if choix_couleur == couleur_gagnante:
            gains = mise * 2
            joueur.augmenter_solde(gains)
            print(f"Félicitations {joueur.nom.strip().capitalize()} ! Tu as gagné {gains}€.\n")
        else:
            joueur.diminuer_solde(mise)
            print(f"Dommage {joueur.nom.strip().capitalize()}, tu as perdu {mise}€.\n")

    def jouer_sur_parite(self, joueur, mise) -> None:
        if mise > joueur.solde:
            print(f"{joueur.nom}, tu n'as pas assez d'argent pour miser {mise}€.\n")
            return

        separateur_roulette = Separateur("-", 69, "+ ")
        separateur_roulette.afficher_separateur()
        print("+ Pair      : 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36")
        print("+ Impair    : 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35")
        separateur_roulette.afficher_separateur()

        parite_gagnante = choice(["Pair", "Impair"])
        choix_parite = input("Choisissez une parité (Pair/Impair) : ").lower()

        print(f"\nLa parité gagnante est : {parite_gagnante}\n")

        if choix_parite == parite_gagnante.lower():
            gains = mise * 2
            joueur.augmenter_solde(gains)
            print(f"Félicitations {joueur.nom.strip().capitalize()} ! Tu as gagné {gains}€.\n")
        else:
            joueur.diminuer_solde(mise)
            print(f"Dommage {joueur.nom.strip().capitalize()}, tu as perdu {mise}€.\n")

    def jouer_sur_groupe(self, joueur, mise) -> None:
        if mise > joueur.solde:
            print(f"{joueur.nom}, tu n'as pas assez d'argent pour miser {mise}€.\n")
            return

        separateur_roulette = Separateur("-", 69, "+ ")

        separateur_roulette.afficher_separateur()
        print("+ 1-12      : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12")
        print("+ 13-24     : 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24")
        print("+ 25-36     : 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36")
        separateur_roulette.afficher_separateur()

        groupe_gagnant = choice(["1-12", "13-24", "25-36"])

        choix_groupe = input("Choisissez un groupe de nombres (1-12, 13-24, 25-36) : ")

        print(f"\nLe groupe gagnant est : {groupe_gagnant}\n")

        if choix_groupe == groupe_gagnant:
            gains = mise * 3
            joueur.augmenter_solde(gains)
            print(f"Félicitations {joueur.nom.strip().capitalize()} ! Tu as gagné {gains}€.\n")
        else:
            joueur.diminuer_solde(mise)
            print(f"Dommage {joueur.nom.strip().capitalize()}, tu as perdu {mise}€.\n")


    def jouer_sur_douzaine(self, joueur, mise) -> None:
        if mise > joueur.solde:
            print(f"{joueur.nom}, tu n'as pas assez d'argent pour miser {mise}€.\n")
            return

        separateur_roulette = Separateur("-", 69, "+ ")

        separateur_roulette.afficher_separateur()
        print("+ 1-12      : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12")
        print("+ 13-24     : 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24")
        print("+ 25-36     : 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36")
        separateur_roulette.afficher_separateur()

        douzaine_gagnante = choice(["1-12", "13-24", "25-36"])

        choix_douzaine = input("Choisissez une douzaine (1-12, 13-24, 25-36) : ")

        print(f"\nLa douzaine gagnante est : {douzaine_gagnante}\n")

        if choix_douzaine == douzaine_gagnante:
            gains = mise * 1.5
            joueur.augmenter_solde(gains)
            print(f"Félicitations {joueur.nom.strip().capitalize()} ! Tu as gagné {gains}€.\n")
        else:
            joueur.diminuer_solde(mise)
            print(f"Dommage {joueur.nom.strip().capitalize()}, tu as perdu {mise}€.\n")
