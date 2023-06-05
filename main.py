#!/usr/bin/env python3

from utilisateur import Utilisateur
from utils.common import *

# PROGRAMME PRINCIPAL
def main():
    scores = Utilitaires.initialisation_scores()
    
    print("\n")
    separateur_tirets_x35_avec_decorateur_plus.afficher_separateur()
    print(""" + TP - D33 (PGR) - MINI CASINO""")
    separateur_tirets_x35_avec_decorateur_plus.afficher_separateur()

    username = input(" + Pour commencer, veuillez saisir votre pseudonyme pour pouvoir jouer : ").upper()

    if username in scores:
        joueur = Utilisateur(username, scores[username])
    else:
        joueur = Utilisateur(username)
        scores[username] = joueur.get_solde()
        Utilitaires.nouveau_scores(username, joueur.get_solde())

    # Message d'accueil
    print(f"\nBienvenue {joueur.get_nom()}, votre solde est de {joueur.get_solde()}€\n")
    
    Utilitaires.afficher_menu(joueur)

# INITIALISATION DU PROGRAMME PRINCIPAL
try:
    main()
except UnboundLocalError:
    scores = Utilitaires.initialisation_scores()
    main()

# Zone de test
Utilitaires.initialisation_scores()
