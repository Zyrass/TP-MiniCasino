#!/usr/bin/env python3

from user import User
from utils.check_files import bienvenue, séparateur, espace, initialisation_scores, nouveau_scores 

# PROGRAMME PRINCIPAL
def main():
    scores = initialisation_scores()
    
    espace()
    séparateur()
    bienvenue()
    séparateur()
    
    username = input(" + Pour commencer, veuillez saisir votre pseudonyme utilisé pour pouvoir jouer: ").upper()

    if username in scores:
        player = User(username, scores[username])
    else:
        player = User(username)
        scores[username] = player._solde
        nouveau_scores(username, player._solde)

    # Message d'accueil
    print(f"\nBienvenue {player._name}, votre solde est de {player._solde}€\n")
    
    while True:
        séparateur("-", 35)
        print(" + MENU - MINI CASINO")
        séparateur("-", 35)
        print(" + 1. Machine à sous")
        print(" + 2. Roulette")
        séparateur("-", 35)
        print(" + Q. Quitter le mini casino")
        séparateur("-", 35)
        
        choix_utilisateur: str = input(f"\n{player._name.strip().capitalize()}, veuillez saisir un choix: ")
        
        if choix_utilisateur == "1":
            pass
        elif choix_utilisateur == "2":
            pass
        elif choix_utilisateur.lower() == "q":
            break
        else:
            print("\n Désolé, ce choix est invalide, veuillez réessayer.\n") 


# INITIALISATION DU PROGRAMME PRINCIPAL
try:
    main()
except UnboundLocalError:
    scores = initialisation_scores()
    main()

# Zone de test
initialisation_scores()
