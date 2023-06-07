from .separateur import Separateur
from jeux.machine_a_sous import MachineASous
from jeux.roulette import Roulette
from os import system


class Menu(Separateur):
    _titre: str
    _choix_1: str
    _choix_2: str
    _quitter: str

    def __init__(self, titre: str = "+ 📍 MENU - MINI CASINO", choix1: str = "+ 1. ➡️   Machine à sous", choix2: str = "+ 2. ➡️   Roulette", quitter: str = "+ Q. ⏹️   Quitter le mini casino") -> None:
        super().__init__("-", 69, "+ ")
        self._titre = titre
        self._choix_1 = choix1
        self._choix_2 = choix2
        self._quitter = quitter

    def afficher_titre(self) -> None:
        print(self._titre)

    def afficher_choix_1(self) -> None:
        print(self._choix_1)

    def afficher_choix_2(self) -> None:
        print(self._choix_2)

    def afficher_quitter(self) -> None:
        print(self._quitter)

    def afficher_menu(self, joueur) -> None:
        while True:
            self.afficher_separateur()
            self.afficher_titre()
            self.afficher_separateur()
            self.afficher_choix_1()
            self.afficher_choix_2()
            self.afficher_separateur()
            self.afficher_quitter()
            self.afficher_separateur()

            choix_utilisateur: str = input(
                f"\n{joueur.get_nom().strip().capitalize()}, veuillez saisir un choix: ")
            print("\n")

            if choix_utilisateur == "1":
                machine = MachineASous()
                machine.run(joueur)
            elif choix_utilisateur == "2":
                roulette = Roulette()
                roulette.run(joueur)
            elif choix_utilisateur.lower() == "q":
                
                print(f"Au revoir {joueur.get_nom()}, à bientôt j'espère.\n")
                break
            else:
                print(
                    f"Désolé {joueur.get_nom().strip().capitalize()}, ce choix est invalide, veuillez réessayer.\n")
