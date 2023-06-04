#!/usr/bin/env python3

from utilisateurs import Utilisateur
from utilitaires import espace, separateur, bienvenue, initialisation_scores, nouveau_scores, afficher_menu

# PROGRAMME PRINCIPAL
def main():
    scores = initialisation_scores()
    
    espace()
    separateur()
    bienvenue()
    separateur()
    
    username = input(" + Pour commencer, veuillez saisir votre pseudonyme pour pouvoir jouer : ").upper()

    if username in scores:
        player = Utilisateur(username, scores[username])
    else:
        player = Utilisateur(username)
        scores[username] = player._solde
        nouveau_scores(username, player._solde)

    # Message d'accueil
    print(f"\nBienvenue {player._name}, votre solde est de {player._solde}€\n")
    
    afficher_menu(player)

# INITIALISATION DU PROGRAMME PRINCIPAL
try:
    main()
except UnboundLocalError:
    scores = initialisation_scores()
    main()

# Zone de test
initialisation_scores()
