from user import User
from .jeu import Jeu
from random import randint

class Roulette(Jeu):
    """Un jeu du mini casino permettant de jouer à la roulette."""
    
    def __init__(self) -> None:
        super().__init__("Roulette")
        
    def run(self, player: User):
        self.bienvenue()
        
        while True:
            
            choix_utilisateur = input(f"\n {player._name}, entre le montant de ta mise (ou q pour quitter) : ")
            if choix_utilisateur.lower() == 'q':
                break
            else:
                mise_départ = int(choix_utilisateur)
                
            if mise_départ > player._solde:
                print(f"\nDésolé {player._name}, tu ne peux pas miser plus que ton solde. Réessayez.")
                print(f"Tu as saisie: {mise_départ} alors qu'il ne te reste que {player._solde}")
                continue
            
            # Si c'est OK on décrémente la valeur saisie
            player.decrement_solde(mise_départ)
            
            choix_nombre_entre_0_et_49 = int(input("Super, choisis maintenant un numéro entre 0 et 49 : "))
            result = randint(0, 0)
            
            print(f"Résultat du tirage: {result}")
            print(f"Tu as choisi: {choix_nombre_entre_0_et_49}")
            
            if result == choix_nombre_entre_0_et_49:
                print(f"Félicitations ! Vous avez gagné {mise_départ * 3}€")
                player.increment_solde(mise_départ * 3)
            elif result % 2 == choix_nombre_entre_0_et_49 % 2:
                print("Vous récupérez la moitié de votre mise.")
                player.increment_solde(mise_départ // 2)
            else:
                print("Désolé, vous avez perdu. Essayez encore !")
