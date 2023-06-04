from .jeu import Jeu
from ..utilisateurs import Utilisateur
from random import randint

class Roulette(Jeu):
    """Un jeu du mini casino permettant de jouer à la roulette."""
    
    def __init__(self):
        super().__init__("Roulette")
        
    def run(self, player: Utilisateur):
        self.bienvenue()
        
        while True:
            
            choix_utilisateur = input(f"\n {player._name}, entre le montant de ta mise (ou q pour quitter) : ")
            if choix_utilisateur.lower() == 'q':
                break
            else:
                mise_depart = int(choix_utilisateur)
                
            if mise_depart > player._solde:
                print(f"\nDésolé {player._name}, tu ne peux pas miser plus que ton solde. Réessaie.")
                print(f"Tu as saisi : {mise_depart} alors qu'il ne te reste que {player._solde}")
                continue
            
            # Si c'est OK, on décrémente la valeur saisie
            player.diminuer_solde(mise_depart)
            
            choix_nombre_entre_0_et_49 = int(input("Super, choisis maintenant un numéro entre 0 et 49 : "))
            resultat = randint(0, 49)
            
            print(f"Résultat du tirage : {resultat}")
            print(f"Tu as choisi : {choix_nombre_entre_0_et_49}")
            
            if resultat == choix_nombre_entre_0_et_49:
                print(f"Félicitations ! Vous avez gagné {mise_depart * 3}€")
                player.augmenter_solde(mise_depart * 3)
            elif resultat % 2 == choix_nombre_entre_0_et_49 % 2:
                print("Vous récupérez la moitié de votre mise.")
                player.augmenter_solde(mise_depart // 2)
            else:
                print("Désolé, vous avez perdu. Essayez encore !")
