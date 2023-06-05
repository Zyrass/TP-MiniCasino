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
        
    def get_titre(self):
        print(f"{self._titre}")
    
    def get_choix_1(self):
        print(f"{self._choix_1}")
    
    def get_choix_2(self):
        print(f"{self._choix_2}")
    
    def get_quitter(self):
        print(f"{self._quitter}")
    
    def afficher_menu(self, joueur):
        Separateur().afficher_separateur()
        self.get_titre()
        Separateur().afficher_separateur()
        self.get_choix_1()
        self.get_choix_2()
        Separateur().afficher_separateur()
        self.get_quitter()
        Separateur().afficher_separateur()
        
        choix_utilisateur: str = input(f"\n{joueur.get_nom().strip().capitalize()}, veuillez saisir un choix: ")
        print("\n")
        
        if choix_utilisateur == "1":
            machine = MachineASous()
            machine.run(joueur)
        elif choix_utilisateur == "2":
            roulette = Roulette()
            roulette.run(joueur)
        elif choix_utilisateur.lower() == "q":
            # Sauvegarde de la nouvelle valeur du solde du joueur
            self.scores[joueur.get_nom()] = joueur.get_solde()
            self.nouveau_scores(joueur.get_nom(), joueur.get_solde())
            return
        else:
            return "\n Désolé, ce choix est invalide, veuillez réessayer.\n"
            