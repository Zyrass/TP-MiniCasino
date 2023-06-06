from .jeu import Jeu
from random import randint
from os import system

class Roulette(Jeu):
    """Un jeu du mini casino permettant de jouer à la roulette."""
    
    def __init__(self):
        super().__init__("Roulette")
        
    def run(self, joueur):
        self.afficher_bienvenue()
        
        while True:
            choix_utilisateur = input(f"\n {joueur.get_nom()}, entre le montant de ta mise (ou q pour quitter) : ")
            if choix_utilisateur.lower() == 'q':
                system("clear")
                return False
            else:
                try:
                    mise_depart = int(choix_utilisateur)
                except ValueError:
                    print("Mise invalide. Veuillez entrer un nombre entier.")
                    continue
                
            if mise_depart > joueur.get_solde():
                print(f"\nDésolé {joueur.get_nom()}, tu ne peux pas miser plus que ton solde. Réessaie.")
                print(f"Tu as saisi : {mise_depart} alors qu'il ne te reste que {joueur.get_solde()}")
                continue
            
            joueur.diminuer_solde(mise_depart)
            
            choix_nombre_entre_0_et_49 = input("Super, choisis maintenant un numéro entre 0 et 49 : ")
            try:
                choix_nombre_entre_0_et_49 = int(choix_nombre_entre_0_et_49)
            except ValueError:
                print("Choix invalide. Veuillez entrer un nombre entier entre 0 et 49.")
                continue
            
            resultat = randint(0, 49)
            
            print(f"Résultat du tirage : {resultat}")
            print(f"Tu as choisi : {choix_nombre_entre_0_et_49}")
            
            if resultat == choix_nombre_entre_0_et_49:
                gain = mise_depart * 3
                print(f"Félicitations ! Vous avez gagné {gain}€")
                joueur.augmenter_solde(gain)
            elif resultat % 2 == choix_nombre_entre_0_et_49 % 2:
                gain = mise_depart // 2
                print("Vous récupérez la moitié de votre mise.")
                joueur.augmenter_solde(gain)
            else:
                print("Désolé, vous avez perdu. Essayez encore !")
