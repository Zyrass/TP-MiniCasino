from utils.common import Separateur
from jeux.machine_a_sous import MachineASous
from jeux.roulette import Roulette

class Menu:
    _titre: str
    _choix_1: str
    _choix_2: str
    _quitter: str
    
    def __init__(self, titre: str = "+ MENU - MINI CASINO", choix1: str = " + 1. Machine à sous", choix2: str = " + 2. Roulette", quitter: str = " + Q. Quitter le mini casino") -> None:
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
        Separateur().afficher_separateur()
        self.afficher_titre()
        Separateur().afficher_separateur()
        self.afficher_choix_1()
        self.afficher_choix_2()
        Separateur().afficher_separateur()
        self.afficher_quitter()
        Separateur().afficher_separateur()
        
        choix_utilisateur: str = input(f"\n{joueur.get_nom().strip().capitalize()}, veuillez saisir un choix: ")
        print("\n")
        
        while True:
            if choix_utilisateur == "1":
                machine = MachineASous()
                machine.run(joueur)
            elif choix_utilisateur == "2":
                roulette = Roulette()
                roulette.run(joueur)
            elif choix_utilisateur.lower() == "q":
                break
            else:
                print("\n Désolé, ce choix est invalide, veuillez réessayer.\n")
